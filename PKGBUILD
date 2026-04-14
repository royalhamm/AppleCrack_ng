# Maintainer: Security Research Team <security@example.com>                                                                                                                     
                                                                                                                                                                                
pkgname=applecrack-ng                                                                                                                                                           
                                                                                                                                                                                
pkgver=0.1.0                                                                                                                                                                    
                                                                                                                                                                                
pkgrel=1                                                                                                                                                                        
                                                                                                                                                                                
pkgdesc="Next Generation iOS Device Management Tool"                                                                                                                            
                                                                                                                                                                                
arch=('any')                                                                                                                                                                    
                                                                                                                                                                                
url="https://github.com/security-team/applecrack_ng"                                                                                                                            
                                                                                                                                                                                
license=('MIT')                                                                                                                                                                 
                                                                                                                                                                                
depends=(                                                                                                                                                                       
                                                                                                                                                                                
    'python'                                                                                                                                                                    
                                                                                                                                                                                
    'python-pyqt5'                                                                                                                                                              
                                                                                                                                                                                
    'python-libimobiledevice'                                                                                                                                                   
                                                                                                                                                                                
    'python-requests'                                                                                                                                                           
                                                                                                                                                                                
    'python-click'                                                                                                                                                              
                                                                                                                                                                                
    'python-tqdm'                                                                                                                                                               
                                                                                                                                                                                
    'python-colorama'                                                                                                                                                           
                                                                                                                                                                                
    'libimobiledevice'                                                                                                                                                          
                                                                                                                                                                                
    'libusbmuxd'                                                                                                                                                                
                                                                                                                                                                                
    'ideviceinstaller'                                                                                                                                                          
                                                                                                                                                                                
    'libideviceactivation'                                                                                                                                                      
                                                                                                                                                                                
    'openssh'                                                                                                                                                                   
                                                                                                                                                                                
    ' paramiko'                                                                                                                                                                 
                                                                                                                                                                                
)                                                                                                                                                                               
                                                                                                                                                                                
optdepends=(                                                                                                                                                                    
                                                                                                                                                                                
    'checkra1n: For checkra1n jailbreak support'                                                                                                                                
                                                                                                                                                                                
    'palera1n: For palera1n jailbreak support'                                                                                                                                  
                                                                                                                                                                                
    'odysseyra1n: For odysseyra1n jailbreak support'                                                                                                                            
                                                                                                                                                                                
    'metasploit: For advanced exploitation'                                                                                                                                     
                                                                                                                                                                                
    'frida: For dynamic instrumentation'                                                                                                                                        
                                                                                                                                                                                
    'mitmproxy: For traffic interception'                                                                                                                                       
                                                                                                                                                                                
    'burpsuite: For web application testing'                                                                                                                                    
                                                                                                                                                                                
)                                                                                                                                                                               
                                                                                                                                                                                
source=("https://github.com/security-team/applecrack_ng/archive/v${pkgver}.tar.gz")                                                                                             
                                                                                                                                                                                
sha256sums=('SKIP')                                                                                                                                                             
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
build() {                                                                                                                                                                       
                                                                                                                                                                                
    cd "${srcdir}/${pkgname}-${pkgver}"                                                                                                                                         
                                                                                                                                                                                
    python setup.py build                                                                                                                                                       
                                                                                                                                                                                
}                                                                                                                                                                               
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
package() {                                                                                                                                                                     
                                                                                                                                                                                
    cd "${srcdir}/${pkgname}-${pkgver}"                                                                                                                                         
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
    # Install Python package                                                                                                                                                    
                                                                                                                                                                                
    python setup.py install --root="${pkgdir}" --optimize=1                                                                                                                     
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
    # Install desktop entry                                                                                                                                                     
                                                                                                                                                                                
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/assets/applecrack_ng.desktop" \                                                                                              
                                                                                                                                                                                
        "${pkgdir}/usr/share/applications/applecrack_ng.desktop"                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
    # Install icons                                                                                                                                                             
                                                                                                                                                                                
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/assets/icon.png" \                                                                                                           
                                                                                                                                                                                
        "${pkgdir}/usr/share/icons/hicolor/256x256/apps/applecrack-ng-icon.png"                                                                                                 
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
    # Install license                                                                                                                                                           
                                                                                                                                                                                
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" \                                                                                                                   
                                                                                                                                                                                
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"                                                                                                                       
                                                                                                                                                                                
}
