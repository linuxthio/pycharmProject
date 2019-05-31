from PyQt5.QtMultimedia import QCamera,QCameraViewfinderSettings




camera = QCamera()
viewfinder =  QCameraViewfinderSettings()
camera.setViewfinder(viewfinder)
viewfinder.show()

camera.start()