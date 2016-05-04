from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.classinfo import check4firmware
from nanpy.memo import memoized


@check4firmware
class Esp(FirmwareClass):
    firmware_id = 'Esp'

    @arduinomethod
    def wdtEnable(self):
        pass

    @arduinomethod
    def wdtDisable(self):
        pass

    @arduinomethod
    def wdtFeed(self):
        pass

    @arduinomethod
    def reset(self):
        pass

    @arduinomethod
    def restart(self):
        pass

    @returns(int)
    @arduinomethod
    def getVcc(self):
        pass

    @arduinomethod
    def getFreeHeap(self):
        pass

    @arduinomethod
    def getChipId(self):
        pass

    @arduinomethod
    def getSdkVersion(self):
        pass

    @arduinomethod
    def getBootVersion(self):
        pass

    @arduinomethod
    def getBootMode(self):
        pass

    @arduinomethod
    def getCpuFreqMHz(self):
        pass

    @arduinomethod
    def getFlashChipId(self):
        pass

    @arduinomethod
    def getFlashChipRealSize(self):
        pass

    @arduinomethod
    def getFlashChipSize(self):
        pass

    @arduinomethod
    def getFlashChipSpeed(self):
        pass

    @arduinomethod
    def getFlashChipMode(self):
        pass

    @arduinomethod
    def getFlashChipSizeByChipId(self):
        pass

    @arduinomethod
    def getResetReason(self):
        pass

    @arduinomethod
    def getResetInfo(self):
        pass

    @arduinomethod
    def getSketchSize(self):
        pass

    @arduinomethod
    def getFreeSketchSpace(self):
        pass

    @arduinomethod
    def flashEraseSector(self):
        pass

    @arduinomethod
    def flashWrite(self):
        pass

    @arduinomethod
    def flashRead(self):
        pass
