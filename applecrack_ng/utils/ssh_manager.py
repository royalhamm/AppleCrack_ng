import paramiko

from PyQt5.QtCore import QObject, pyqtSignal, QThread



class SSHManager(QObject):

    output = pyqtSignal(str)



    def __init__(self, host, port=22, username='root', password=None, key_filename=None):

        super().__init__()

        self.host = host

        self.port = port

        self.username = username

        self.password = password

        self.key_filename = key_filename

        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.channel = None



    def connect(self):

        try:

            self.client.connect(self.host, port=self.port, username=self.username, password=self.password, key_filename=self.key_filename)

            self.channel = self.client.invoke_shell()

            self.channel.settimeout(0.1)

            self.output.emit("SSH connection established.")

        except Exception as e:

            self.output.emit(f"Failed to connect: {e}")



    def send_command(self, command):

        if self.channel is not None:

            self.channel.send(command + "\n")



    def read_output(self):

        while True:

            try:

                if self.channel.recv_ready():

                    output = self.channel.recv(1024).decode('utf-8')

                    self.output.emit(output)

            except Exception as e:

                self.output.emit(f"Error reading output: {e}")

                break



    def disconnect(self):

        if self.client is not None:

            self.client.close()

            self.output.emit("SSH connection closed.")
