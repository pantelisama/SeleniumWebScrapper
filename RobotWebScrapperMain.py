from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

## PANTELIS PANTELIDIS CMC.ini / PERFORMANCE.ini reader and cmc v2 web interface scrapper of settings ###
######################################################################################################################################### CMC.INI/PERFORMANCE.INI DATA COLLECTION
list = []
variable_name = [] # cmc.ini variable names
variable_values = [] # cmc.ini variable values
list2 = []
variable_nameP = [] # performance.ini variable names
variable_valuesP = [] # performance.ini variable values
GeneralPageV = []
NetworkPageV = []
PanPageV = []
TiltPageV = []
HeightPageV = []
TrackPageV = []
LensPageV = []
RobotPageV = []
VRPageV = []
GeneralPage = []
NetworkPage = []
PanPage = []
TiltPage = []
HeightPage = []
TrackPage = []
LensPage = []
RobotPage = []
VRPage = []

with open('cmcini.text','r') as f:
    for line in f:
        list.append(line)
    #print(len(list))
    for i in range(0,len(list),2):
        variable_name.append(list[i])
        #print(variable_name)
    for i in range(1,len(list),2):
        variable_values.append(list[i])

with open('performanceini.text','r') as f:
    for line in f:
        list2.append(line)
    #print(len(list))
    for i in range(0,len(list2),2):
        variable_nameP.append(list2[i])
        #print(variable_name)
    for i in range(1,len(list2),2):
        variable_valuesP.append(list2[i])

variable_name = [r.strip() for r in variable_name]
variable_nameP = [r.strip() for r in variable_nameP]
variable_values = [r.strip() for r in variable_values]
variable_valuesP = [r.strip() for r in variable_valuesP]


# for i in range(0,len(variable_name)):
#     print(variable_name[i].strip(), ":",variable_values[i].strip())

# for i in range(0,len(variable_nameP)):
#     print(variable_nameP[i].strip(), ":",variable_valuesP[i].strip())
#
# print(len(variable_name+variable_nameP)) # print all CMC V1 settings
settings_names = variable_name+variable_nameP
settings_values = variable_values+variable_valuesP
####################################################################################################################################### CMC.INI/PERFORMANCE.INI DATA COLLECTION



################################################################################################################################################################### WEB SCRAPER


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("http://192.1.0.131/Web/General.htm")
driver.implicitly_wait(6)

############################################################################################################################ GENERAL PAGE 1
CameraNumber = driver.find_element(By.XPATH, "//input[@id='CamNum']").get_attribute('value')
HeadModel = driver.find_element(By.XPATH, "//input[@id='HeadModel']").get_attribute('value')
HeightModel = driver.find_element(By.XPATH, "//input[@id='HeightModel']").get_attribute('value')
TrackModel = driver.find_element(By.XPATH, "//tbody/tr[4]/td[1]").get_attribute('value')
AllowHeightOnly = driver.find_element(By.XPATH, "//input[@id='HeightOnly']").get_attribute('value')
ControlCameraCCU = driver.find_element(By.XPATH, "//input[@id='CMCWithNHM']").get_attribute('value')
ControlTRP100 = driver.find_element(By.XPATH, "//input[@id='UseRobot']").get_attribute('value')
ControlSmartped = driver.find_element(By.XPATH, "//input[@id='UseSmartPed']").get_attribute('value')

General1 = [CameraNumber,HeadModel,HeightModel,TrackModel,AllowHeightOnly,ControlCameraCCU,ControlTRP100,ControlSmartped]


CameraNumberT = driver.find_element(By.XPATH, "//td[normalize-space()='Camera Number']").text
HeadModelT = driver.find_element(By.XPATH, "//td[normalize-space()='Head Model']").text
HeightModelT = driver.find_element(By.XPATH, "//td[normalize-space()='Height Model']").text
TrackModelT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Model']").text
AllowHeightOnlyT = driver.find_element(By.XPATH, "//td[normalize-space()='Allow Height Only']").text
ControlCameraCCUT = driver.find_element(By.XPATH, "//td[normalize-space()='Control Camera/CCU']").text
ControlTRP100T = driver.find_element(By.XPATH, "//td[normalize-space()='Control TRP100']").text
ControlSmartpedT = driver.find_element(By.XPATH, "//td[normalize-space()='Control SmartPed']").text

General1S = [CameraNumberT,HeadModelT,HeightModelT,TrackModelT,AllowHeightOnlyT,ControlCameraCCUT,ControlTRP100T,ControlSmartpedT]



############################################################################################################################ GENERAL PAGE 1

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ GENERAL PAGE 2

AccelerationAtLimit = driver.find_element(By.XPATH, "//input[@id='AccAtLimit']").get_attribute('value')
ADCOn = driver.find_element(By.XPATH, "//input[@id='ADCon']").get_attribute('value')
CheckLocalRemote = driver.find_element(By.XPATH, "//input[@id='CheckLocRem']").get_attribute('value')
DeleteLimitFiles = driver.find_element(By.XPATH, "//input[@id='DelLimFiles']").get_attribute('value')
EnableDisplay = driver.find_element(By.XPATH, "//tbody/tr[5]/td[1]").get_attribute('value')
HandControlsDirect = driver.find_element(By.XPATH, "//input[@id='HCdirect']").get_attribute('value')
HeadLatency = driver.find_element(By.XPATH, "//input[@id='HeadLatency']").get_attribute('value')
JoystickVelocity = driver.find_element(By.XPATH, "//input[@id='JSvelocity']").get_attribute('value')

General2 = [AccelerationAtLimit,ADCOn,CheckLocalRemote,DeleteLimitFiles,EnableDisplay,HandControlsDirect,HeadLatency,JoystickVelocity]

AccelerationAtLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Acceleration at Limit']").text
ADCOnT = driver.find_element(By.XPATH, "//td[normalize-space()='Acceleration at Limit']").text
CheckLocalRemoteT = driver.find_element(By.XPATH, "//td[normalize-space()='Check Local/Remote']").text
DeleteLimitFilesT = driver.find_element(By.XPATH, "//td[normalize-space()='Delete Limit Files']").text
EnableDisplayT = driver.find_element(By.XPATH, "//td[normalize-space()='Enable Display']").text
HandControlsDirectT = driver.find_element(By.XPATH, "//td[normalize-space()='Hand Controls Direct']").text
HeadLatencyT = driver.find_element(By.XPATH, "//td[normalize-space()='Head Latency']").text
JoystickVelocityT = driver.find_element(By.XPATH, "//td[normalize-space()='Joystick Velocity']").text

General2S = [AccelerationAtLimitT,ADCOnT,CheckLocalRemoteT,DeleteLimitFilesT,EnableDisplayT,HandControlsDirectT,HeadLatencyT,JoystickVelocityT]


############################################################################################################################ GENERAL PAGE 2

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ GENERAL PAGE 3

LimitDistance = driver.find_element(By.XPATH, "//input[@id='LimitDist']").get_attribute('value')
LimitTimeWindow = driver.find_element(By.XPATH, "//input[@id='LimitTime']").get_attribute('value')
NewSeQMethod = driver.find_element(By.XPATH, "//input[@id='NewSeq']").get_attribute('value')
PositionalTrimSmoothing = driver.find_element(By.XPATH, "//input[@id='PosTrimSF']").get_attribute('value')
RelayDriveMode = driver.find_element(By.XPATH, "//input[@id='RelayMode']").get_attribute('value')
SamplelTime = driver.find_element(By.XPATH, "//input[@id='SampTime']").get_attribute('value')
SeqNth = driver.find_element(By.XPATH, "//input[@id='SeqNth']").get_attribute('value')
StartupDelay = driver.find_element(By.XPATH, "//input[@id='SeqNth']").get_attribute('value')

General3 = [LimitDistance,LimitTimeWindow,NewSeQMethod,PositionalTrimSmoothing,RelayDriveMode,SamplelTime,SeqNth,StartupDelay]

LimitDistanceT = driver.find_element(By.XPATH, "//td[normalize-space()='Limit Distance']").text
LimitTimeWindowT = driver.find_element(By.XPATH, "//td[normalize-space()='Limit Time Window']").text
NewSeQMethodT = driver.find_element(By.XPATH, "//td[normalize-space()='New Sequence Method']").text
PositionalTrimSmoothingT = driver.find_element(By.XPATH, "//td[normalize-space()='Positional Trim Smoothing']").text
RelayDriveModeT = driver.find_element(By.XPATH, "//td[normalize-space()='Relay Drive Mode']").text
SamplelTimeT = driver.find_element(By.XPATH, "//td[normalize-space()='Sample Time']").text
SeqNthT = driver.find_element(By.XPATH, "//td[normalize-space()='Sequence Nth']").text
StartupDelayT = driver.find_element(By.XPATH, "//td[normalize-space()='Startup Delay']").text

General3S = [LimitDistanceT,LimitTimeWindowT,NewSeQMethodT,PositionalTrimSmoothingT,RelayDriveModeT,SamplelTimeT,SeqNthT,StartupDelayT]

############################################################################################################################ GENERAL PAGE 3

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ GENERAL PAGE 4

ToggleAtStore = driver.find_element(By.XPATH, "//input[@id='ToggleStore']").get_attribute('value')
ZOffRatio = driver.find_element(By.XPATH, "//input[@id='ZOffRatio']").get_attribute('value')
ZoneDeadband = driver.find_element(By.XPATH, "//input[@id='ZoneDB']").get_attribute('value')
FaderMultiplier = driver.find_element(By.XPATH, "//input[@id='FaderMult']").get_attribute('value')
LoggingLevel = driver.find_element(By.XPATH, "//input[@id='LogLevel']").get_attribute('value')
Output1Mom = driver.find_element(By.XPATH, "//input[@id='OP1Mom']").get_attribute('value')
Output2Mom = driver.find_element(By.XPATH, "//input[@id='OP2Mom']").get_attribute('value')
Output3Mom = driver.find_element(By.XPATH, "//input[@id='OP3Mom']").get_attribute('value')

General4 = [ToggleAtStore,ZOffRatio,ZoneDeadband,FaderMultiplier,LoggingLevel,Output1Mom,Output2Mom,Output3Mom]

ToggleAtStoreT = driver.find_element(By.XPATH, "//td[normalize-space()='Toggle at Store']").text
ZOffRatioT = driver.find_element(By.XPATH, "//td[normalize-space()='Z-Off Ratio']").text
ZoneDeadbandT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone Deadband']").text
FaderMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Fader Multiplier']").text
LoggingLevelT = driver.find_element(By.XPATH, "//td[normalize-space()='Logging Level']").text
Output1MomT = driver.find_element(By.XPATH, "//td[normalize-space()='Output1 Momentary']").text
Output2MomT = driver.find_element(By.XPATH, "//td[normalize-space()='Output2 Momentary']").text
Output3MomT = driver.find_element(By.XPATH, "//td[normalize-space()='Output3 Momentary']").text

General4S = [ToggleAtStoreT,ZOffRatioT,ZoneDeadbandT,FaderMultiplierT,LoggingLevelT,Output1MomT,Output2MomT,Output3MomT]

############################################################################################################################ GENERAL PAGE 4

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)


############################################################################################################################ GENERAL PAGE 5

PanRetarget = driver.find_element(By.XPATH, "//input[@id='PanRetarget']").get_attribute('value')
RestrictShotWithinLimits = driver.find_element(By.XPATH, "//input[@id='RestrictShot']").get_attribute('value')
UseLearnForLocalRemote = driver.find_element(By.XPATH, "//input[@id='UseLearnLR']").get_attribute('value')
RecordTravel = driver.find_element(By.XPATH, "//input[@id='RecordTravel']").get_attribute('value')

General5 = [PanRetarget,RestrictShotWithinLimits,UseLearnForLocalRemote,RecordTravel]

PanRetargetT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Retarget']").text
RestrictShotWithinLimitsT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Retarget']").text
UseLearnForLocalRemoteT = driver.find_element(By.XPATH, "//td[normalize-space()='Use Learn For Local/Remote']").text
RecordTravelT = driver.find_element(By.XPATH, "//td[normalize-space()='Record Travel']").text

General5S = [PanRetargetT,RestrictShotWithinLimitsT,UseLearnForLocalRemoteT,RecordTravelT]

############################################################################################################################ GENERAL PAGE 5


driver.find_element(By.XPATH, "//a[normalize-space()='Network']").click()
driver.implicitly_wait(2)

############################################################################################################################ NETWORK PAGE 1

IP = driver.find_element(By.XPATH, "//input[@id='IPaddr']").get_attribute('value')
GatewayAddress = driver.find_element(By.XPATH, "//input[@id='GatewayAddr']").get_attribute('value')
SubnetMask = driver.find_element(By.XPATH, "//input[@id='SubnetMask']").get_attribute('value')
CameraSelectInterval = driver.find_element(By.XPATH, "//input[@id='CamSelInterval']").get_attribute('value')
NetworkFullDuplex = driver.find_element(By.XPATH, "//input[@id='NetFullDup']").get_attribute('value')
NetworkSpeed = driver.find_element(By.XPATH, "//input[@id='NetSpeed']").get_attribute('value')
FilterSubnet = driver.find_element(By.XPATH, "//input[@id='FiltSubnet']").get_attribute('value')

Network1 = [IP,GatewayAddress,SubnetMask,CameraSelectInterval,NetworkFullDuplex,NetworkSpeed,FilterSubnet]

IPT = driver.find_element(By.XPATH, "//td[normalize-space()='IP Address']").text
GatewayAddressT = driver.find_element(By.XPATH, "//td[normalize-space()='Gateway Address']").text
SubnetMaskT = driver.find_element(By.XPATH, "//td[normalize-space()='Subnet Mask']").text
CameraSelectIntervalT = driver.find_element(By.XPATH, "//td[normalize-space()='Camera Select Interval']").text
NetworkFullDuplexT = driver.find_element(By.XPATH, "//td[normalize-space()='Network Full Duplex']").text
NetworkSpeedT = driver.find_element(By.XPATH, "//td[normalize-space()='Network Speed']").text
FilterSubnetT = driver.find_element(By.XPATH, "//td[normalize-space()='Filter Subnet']").text

Network1S = [IPT,GatewayAddressT,SubnetMaskT,CameraSelectIntervalT,NetworkFullDuplexT,NetworkSpeedT,FilterSubnetT]

############################################################################################################################ NETWORK PAGE 1


driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

############################################################################################################################ NETWORK PAGE 2

UdpPort1 = driver.find_element(By.XPATH, "//input[@id='UDPport1']").get_attribute('value')
UdpPort2 = driver.find_element(By.XPATH, "//input[@id='UDPport2']").get_attribute('value')
OnAirPort = driver.find_element(By.XPATH, "//input[@id='OnAirPort']").get_attribute('value')
OnAirOutput = driver.find_element(By.XPATH, "//input[@id='OnAirOutput']").get_attribute('value')
ListenPort = driver.find_element(By.XPATH, "//input[@id='ListenPort']").get_attribute('value')
PrivateUdpPort = driver.find_element(By.XPATH, "//input[@id='PrvUDPport']").get_attribute('value')
PrivateListenPort = driver.find_element(By.XPATH, "//input[@id='PrvListenPort']").get_attribute('value')
ServiceInterfacePort = driver.find_element(By.XPATH, "//input[@id='SrvIFport']").get_attribute('value')
CameraSelectBroadcastPort = driver.find_element(By.XPATH, "//input[@id='CamSelPort']").get_attribute('value')

Network2 = [UdpPort1,UdpPort2,OnAirPort,OnAirOutput,ListenPort,PrivateUdpPort,PrivateListenPort,ServiceInterfacePort,CameraSelectBroadcastPort]

UdpPort1T = driver.find_element(By.XPATH, "//td[normalize-space()='UDP Port1']").text
UdpPort2T = driver.find_element(By.XPATH, "//td[normalize-space()='UDP Port2']").text
OnAirPortT = driver.find_element(By.XPATH, "//td[normalize-space()='On Air Port']").text
OnAirOutputT = driver.find_element(By.XPATH, "//td[normalize-space()='On Air Output']").text
ListenPortT = driver.find_element(By.XPATH, "//td[normalize-space()='Listen Port']").text
PrivateUdpPortT = driver.find_element(By.XPATH, "//td[normalize-space()='Private UDP Port']").text
PrivateListenPortT = driver.find_element(By.XPATH, "//td[normalize-space()='Private Listen Port']").text
ServiceInterfacePortT = driver.find_element(By.XPATH, "//td[normalize-space()='Service Interface Port']").text
CameraSelectBroadcastPortT = driver.find_element(By.XPATH, "//td[normalize-space()='Camera Select Broadcast Port']").text

Network2S = [UdpPort1T,UdpPort2T,OnAirPortT,OnAirOutputT,ListenPortT,PrivateUdpPortT,PrivateListenPortT,ServiceInterfacePortT,CameraSelectBroadcastPortT]

############################################################################################################################ NETWORK PAGE 2

driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

############################################################################################################################ NETWORK PAGE 3

RobotPort = driver.find_element(By.XPATH, "//input[@id='RobotPort']").get_attribute('value')
USSeqControlPort = driver.find_element(By.XPATH, "//input[@id='USport']").get_attribute('value')
TcpLogServerPort = driver.find_element(By.XPATH, "//input[@id='LogPort']").get_attribute('value')

Network3 = [RobotPort,USSeqControlPort,TcpLogServerPort]

RobotPortT = driver.find_element(By.XPATH, "//td[normalize-space()='Robot Port']").text
USSeqControlPortT = driver.find_element(By.XPATH, "//td[normalize-space()='U/S Seqence Control Port']").text
TcpLogServerPortT = driver.find_element(By.XPATH, "//td[normalize-space()='TCP Log Server Port']").text

Network3S = [RobotPortT,USSeqControlPortT,TcpLogServerPortT]

############################################################################################################################ NETWORK PAGE 3

driver.find_element(By.XPATH, "//a[normalize-space()='Pan']").click()
driver.implicitly_wait(2)


############################################################################################################################ PAN PAGE 1

PanReverse = driver.find_element(By.XPATH, "//input[@id='PanReverse']").get_attribute('value')
PanDriveInvert = driver.find_element(By.XPATH, "//input[@id='PanReverse']").get_attribute('value')
PanHighLimit = driver.find_element(By.XPATH, "//input[@id='PanHiLimit']").get_attribute('value')
PanLowLimit = driver.find_element(By.XPATH, "//input[@id='PanLoLimit']").get_attribute('value')
PanJsMedium = driver.find_element(By.XPATH, "//input[@id='PanMedium']").get_attribute('value')
PanJsFine = driver.find_element(By.XPATH, "//input[@id='PanFine']").get_attribute('value')
PanMultiplier = driver.find_element(By.XPATH, "//input[@id='PanMultFact']").get_attribute('value')

Pan1 = [PanReverse,PanDriveInvert,PanHighLimit,PanLowLimit,PanJsMedium,PanJsFine,PanMultiplier]

PanReverseT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Reverse']").text
PanDriveInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Drive Invert']").text
PanHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan High Limit']").text
PanLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Low Limit']").text
PanJsMediumT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan JS Medium']").text
PanJsFineT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan JS Fine']").text
PanMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Multiplier']").text

Pan1S = [PanReverseT,PanDriveInvertT,PanHighLimitT,PanLowLimitT,PanJsMediumT,PanJsFineT,PanMultiplierT]

############################################################################################################################ PAN PAGE 1


driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)
############################################################################################################################ PAN PAGE 2

DerivativeTime = driver.find_element(By.XPATH, "//input[@id='PanDT']").get_attribute('value')
IntegrationLimit = driver.find_element(By.XPATH, "//input[@id='PanIL']").get_attribute('value')
AccelFeedForward = driver.find_element(By.XPATH, "//input[@id='PanKAFF']").get_attribute('value')
KD = driver.find_element(By.XPATH, "//input[@id='PanKD']").get_attribute('value')
KI = driver.find_element(By.XPATH, "//input[@id='PanKI']").get_attribute('value')
KP = driver.find_element(By.XPATH, "//input[@id='PanKP']").get_attribute('value')
VelocityFeedForward = driver.find_element(By.XPATH, "//input[@id='PanKVFF']").get_attribute('value')
InterpolationFactor = driver.find_element(By.XPATH, "//input[@id='PanInterp']").get_attribute('value')
MaximumAccel = driver.find_element(By.XPATH, "//input[@id='PanMaxAcc']").get_attribute('value')
MaximumVel = driver.find_element(By.XPATH, "//input[@id='PanMaxVel']").get_attribute('value')
MinimumAccel = driver.find_element(By.XPATH, "//input[@id='PanMinAcc']").get_attribute('value')
ProfileSubmode = driver.find_element(By.XPATH, "//input[@id='PanPSubMode']").get_attribute('value')

Pan2 = [DerivativeTime,IntegrationLimit,AccelFeedForward,KD,KI,KP,VelocityFeedForward,InterpolationFactor,MaximumAccel,MaximumVel,MinimumAccel,ProfileSubmode]

DerivativeTimeT = driver.find_element(By.XPATH, "//td[normalize-space()='Derivative Time']").text
IntegrationLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Integration Limit']").text
AccelFeedForwardT = driver.find_element(By.XPATH, "//td[normalize-space()='Accel Feed Forward']").text
KDT= driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KD']").text
KIT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KI']").text
KPT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KP']").text
VelocityFeedForwardT = driver.find_element(By.XPATH, "//td[normalize-space()='Velocity Feed Forward']").text
InterpolationFactorT = driver.find_element(By.XPATH, "//td[normalize-space()='Interpolation Factor']").text
MaximumAccelT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Acceleration']").text
MaximumVelT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Velocity']").text
MinimumAccelT = driver.find_element(By.XPATH, "//td[normalize-space()='Minimum Acceleration']").text
ProfileSubmodeT = driver.find_element(By.XPATH, "//td[normalize-space()='Profile Submode']").text


Pan2S = [DerivativeTimeT,IntegrationLimitT,AccelFeedForwardT,KDT,KIT,KPT,VelocityFeedForwardT,InterpolationFactorT,MaximumAccelT,MaximumVelT,MinimumAccelT,ProfileSubmodeT]

############################################################################################################################ PAN PAGE 2



driver.find_element(By.XPATH, "//a[normalize-space()='Tilt']").click()
driver.implicitly_wait(2)


############################################################################################################################ TILT PAGE 1

TiltReverse = driver.find_element(By.XPATH, "//input[@id='TiltReverse']").get_attribute('value')
TiltDriveInvert = driver.find_element(By.XPATH, "//input[@id='TiltDrvInv']").get_attribute('value')
TiltHighLimit = driver.find_element(By.XPATH, "//input[@id='TiltHiLimit']").get_attribute('value')
TiltLowLimit = driver.find_element(By.XPATH, "//input[@id='TiltLoLimit']").get_attribute('value')
TiltJsMedium = driver.find_element(By.XPATH, "//input[@id='TiltMedium']").get_attribute('value')
TiltJsFine = driver.find_element(By.XPATH, "//input[@id='TiltFine']").get_attribute('value')
TiltMultiplier = driver.find_element(By.XPATH, "//input[@id='TiltMultFact']").get_attribute('value')

Tilt1 = [TiltReverse,TiltDriveInvert,TiltHighLimit,TiltLowLimit,TiltJsMedium,TiltJsFine,TiltMultiplier]

TiltReverseT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt Reverse']").text
TiltDriveInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt Drive Invert']").text
TiltHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt High Limit']").text
TiltLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt Low Limit']").text
TiltJsMediumT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt JS Medium']").text
TiltJsFineT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt JS Fine']").text
TiltMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt Multiplier']").text

Tilt1S = [TiltReverseT,TiltDriveInvertT,TiltHighLimitT,TiltLowLimitT,TiltJsMediumT,TiltJsFineT,TiltMultiplierT]

############################################################################################################################ TILT PAGE 1

driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

############################################################################################################################ TILT PAGE 2

DerivativeTimeT = driver.find_element(By.XPATH, "//input[@id='TiltDT']").get_attribute('value')
IntegrationLimitT = driver.find_element(By.XPATH, "//input[@id='TiltIL']").get_attribute('value')
AccelFeedForwardT = driver.find_element(By.XPATH, "//input[@id='TiltKAFF']").get_attribute('value')
KDT = driver.find_element(By.XPATH, "//input[@id='TiltKD']").get_attribute('value')
KIT = driver.find_element(By.XPATH, "//input[@id='TiltKI']").get_attribute('value')
KPT = driver.find_element(By.XPATH, "//input[@id='TiltKP']").get_attribute('value')
VelocityFeedForwardT = driver.find_element(By.XPATH, "//input[@id='TiltKVFF']").get_attribute('value')
InterpolationFactorT = driver.find_element(By.XPATH, "//input[@id='TiltInterp']").get_attribute('value')
MaximumAccelT = driver.find_element(By.XPATH, "//input[@id='TiltMaxAcc']").get_attribute('value')
MaximumVelT = driver.find_element(By.XPATH, "//input[@id='TiltMaxAcc']").get_attribute('value')
MinimumAccelT = driver.find_element(By.XPATH, "//input[@id='TiltMinAcc']").get_attribute('value')
ProfileSubmodeT = driver.find_element(By.XPATH, "//input[@id='TiltPSubMode']").get_attribute('value')


Tilt2 = [DerivativeTimeT,IntegrationLimitT,AccelFeedForwardT,KDT,KIT,KDT,VelocityFeedForwardT,InterpolationFactorT,MaximumAccelT,MaximumVelT,MinimumAccelT,ProfileSubmodeT]

DerivativeTimeTT = driver.find_element(By.XPATH, "//td[normalize-space()='Derivative Time']").text
IntegrationLimitTT = driver.find_element(By.XPATH, "//td[normalize-space()='Integration Limit']").text
AccelFeedForwardTT = driver.find_element(By.XPATH, "//td[normalize-space()='Integration Limit']").text
KDTT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KD']").text
KITT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KI']").text
KPTT= driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KP']").text
VelocityFeedForwardTT = driver.find_element(By.XPATH, "//td[normalize-space()='Velocity Feed Forward']").text
InterpolationFactorTT = driver.find_element(By.XPATH, "//td[normalize-space()='Interpolation Factor']").text
MaximumAccelTT = driver.find_element(By.XPATH, "//td[normalize-space()='Interpolation Factor']").text
MaximumVelTT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Velocity']").text
MinimumAccelTT = driver.find_element(By.XPATH, "//td[normalize-space()='Minimum Acceleration']").text
ProfileSubmodeTT = driver.find_element(By.XPATH, "//td[normalize-space()='Profile Submode']").text

Tilt2S = [DerivativeTimeTT,IntegrationLimitTT,AccelFeedForwardTT,KDTT,KITT,KDTT,VelocityFeedForwardTT,InterpolationFactorTT,MaximumAccelTT,MaximumVelTT,MinimumAccelTT,ProfileSubmodeTT]

############################################################################################################################ TILT PAGE 2

driver.find_element(By.XPATH, "//a[normalize-space()='Height']").click()
driver.implicitly_wait(2)

############################################################################################################################ HEIGHT PAGE 1


HeightHighLimit = driver.find_element(By.XPATH, "//input[@id='HeightHiLimit']").get_attribute('value')
HeightLowLimit = driver.find_element(By.XPATH, "//input[@id='HeightLoLimit']").get_attribute('value')
HeightJsMedium = driver.find_element(By.XPATH, "//input[@id='HeightMedium']").get_attribute('value')
HeightJsFine = driver.find_element(By.XPATH, "//input[@id='HeightFine']").get_attribute('value')
HeightMultiplier = driver.find_element(By.XPATH, "//input[@id='HeightMultFact']").get_attribute('value')
TransitionZoneLimit = driver.find_element(By.XPATH, "//input[@id='HeightMultFact']").get_attribute('value')
ZoneTargetCoordinates = driver.find_element(By.XPATH, "//input[@id='HeightZTC']").get_attribute('value')
StallDetect = driver.find_element(By.XPATH, "//input[@id='HeightStallDet']").get_attribute('value')
TachoFeedback = driver.find_element(By.XPATH, "//input[@id='HeightTachoFB']").get_attribute('value')


Height1 = [HeightHighLimit,HeightLowLimit,HeightJsMedium,HeightJsFine,HeightMultiplier,TransitionZoneLimit,ZoneTargetCoordinates,StallDetect,TachoFeedback]

HeightHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Height High Limit']").text
HeightLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Height Low Limit']").text
HeightJsMediumT = driver.find_element(By.XPATH, "//td[normalize-space()='Height Low Limit']").text
HeightJsFineT = driver.find_element(By.XPATH, "//td[normalize-space()='Height JS Fine']").text
HeightMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Height Multiplier']").text
TransitionZoneLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Transition Zone Limit']").text
ZoneTargetCoordinatesT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone Target Coordinates']").text
StallDetectT = driver.find_element(By.XPATH, "//td[normalize-space()='Stall Detect']").text
TachoFeedbackT = driver.find_element(By.XPATH, "//td[normalize-space()='Tacho Feedback']").text


Height1S = [HeightHighLimitT,HeightLowLimitT,HeightJsMediumT,HeightJsFineT,HeightMultiplierT,TransitionZoneLimitT,ZoneTargetCoordinatesT,StallDetectT,TachoFeedbackT]

############################################################################################################################ HEIGHT PAGE 2

driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

DerivativeTimeH = driver.find_element(By.XPATH, "//input[@id='HeightDT']").get_attribute('value')
IntegrationLimitH= driver.find_element(By.XPATH, "//input[@id='HeightIL']").get_attribute('value')
AccelFeedForwardH = driver.find_element(By.XPATH, "//input[@id='HeightKAFF']").get_attribute('value')
KDH = driver.find_element(By.XPATH, "//input[@id='HeightKD']").get_attribute('value')
KIH = driver.find_element(By.XPATH, "//input[@id='HeightKI']").get_attribute('value')
KPH = driver.find_element(By.XPATH, "//input[@id='HeightKP']").get_attribute('value')
VelocityFeedForwardH = driver.find_element(By.XPATH, "//input[@id='HeightKVFF']").get_attribute('value')
InterpolationFactorH = driver.find_element(By.XPATH, "//input[@id='HeightInterp']").get_attribute('value')
MaximumAccelH = driver.find_element(By.XPATH, "//input[@id='HeightMaxAcc']").get_attribute('value')
MaximumVelH = driver.find_element(By.XPATH, "//input[@id='HeightMaxVel']").get_attribute('value')
MinimumAccelH = driver.find_element(By.XPATH, "//input[@id='HeightMinAcc']").get_attribute('value')
ProfileSubmodeH = driver.find_element(By.XPATH, "//input[@id='HeightPSubMode']").get_attribute('value')

Height2 = [DerivativeTimeH,IntegrationLimitH,AccelFeedForwardH,KDH,KIH,KPH,VelocityFeedForwardH,InterpolationFactorH,MaximumAccelH,MaximumVelH,MinimumAccelH,ProfileSubmodeH]

DerivativeTimeHT = driver.find_element(By.XPATH, "//td[normalize-space()='Derivative Time']").text
IntegrationLimitHT= driver.find_element(By.XPATH, "//td[normalize-space()='Integration Limit']").text
AccelFeedForwardHT = driver.find_element(By.XPATH, "//td[normalize-space()='Accel Feed Forward']").text
KDHT = driver.find_element(By.XPATH, "//td[normalize-space()='Accel Feed Forward']").text
KIHT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KI']").text
KPHT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KP']").text
VelocityFeedForwardHT = driver.find_element(By.XPATH, "//td[normalize-space()='Velocity Feed Forward']").text
InterpolationFactorHT = driver.find_element(By.XPATH, "//td[normalize-space()='Interpolation Factor']").text
MaximumAccelHT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Acceleration']").text
MaximumVelHT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Velocity']").text
MinimumAccelHT = driver.find_element(By.XPATH, "//td[normalize-space()='Minimum Acceleration']").text
ProfileSubmodeHT = driver.find_element(By.XPATH, "//td[normalize-space()='Profile Submode']").text


Height2S = [DerivativeTimeHT,IntegrationLimitHT,AccelFeedForwardHT,KDHT,KIHT,KPHT,VelocityFeedForwardHT,InterpolationFactorHT,MaximumAccelHT,MaximumVelHT,MinimumAccelHT,ProfileSubmodeHT]

############################################################################################################################ HEIGHT PAGE 2

driver.find_element(By.XPATH, "//a[normalize-space()='Track']").click()
driver.implicitly_wait(2)


############################################################################################################################ TRACK PAGE 1


TrackHighLimit = driver.find_element(By.XPATH, "//input[@id='TrackHiLimit']").get_attribute('value')
TrackLowLimit = driver.find_element(By.XPATH, "//input[@id='TrackHiLimit']").get_attribute('value')
TrackMultiplier = driver.find_element(By.XPATH, "//input[@id='TrackMultFact']").get_attribute('value')
TrackCalibrationDataFile = driver.find_element(By.XPATH, "//input[@id='TrackFile']").get_attribute('value')
UseTrackZones = driver.find_element(By.XPATH, "//input[@id='TrackUseZones']").get_attribute('value')
Zone1highLimit = driver.find_element(By.XPATH, "//input[@id='TrackZ1HiLim']").get_attribute('value')
Zone2LowLimit = driver.find_element(By.XPATH, "//input[@id='TrackZ1LoLim']").get_attribute('value')
Zone3HighLimit = driver.find_element(By.XPATH, "//input[@id='TrackZ3HiLim']").get_attribute('value')
Zone4LowLimit = driver.find_element(By.XPATH, "//input[@id='TrackZ3LoLim']").get_attribute('value')

Track1 = [TrackHighLimit,TrackLowLimit,TrackMultiplier,TrackCalibrationDataFile,UseTrackZones,Zone1highLimit,Zone2LowLimit,Zone3HighLimit,Zone4LowLimit]

TrackHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Track High Limit']").text
TrackLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Low Limit']").text
TrackMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Multiplier']").text
TrackCalibrationDataFileT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Calibration Data File']").text
UseTrackZonesT = driver.find_element(By.XPATH, "//td[normalize-space()='Use Track Zones']").text
Zone1highLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone 1 High Limit']").text
Zone2LowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone 1 Low Limit']").text
Zone3HighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone 3 High Limit']").text
Zone4LowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zone 3 Low Limit']").text


Track1S = [TrackHighLimitT,TrackLowLimitT,TrackMultiplierT,TrackCalibrationDataFileT,UseTrackZonesT,Zone1highLimitT,Zone2LowLimitT,Zone3HighLimitT,Zone4LowLimitT]

############################################################################################################################ TRACK PAGE 1

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)


############################################################################################################################ TRACK PAGE 2

TrackBumper = driver.find_element(By.XPATH, "//input[@id='TrackBumper']").get_attribute('value')
BumperGPIO = driver.find_element(By.XPATH, "//input[@id='BumpGPIO']").get_attribute('value')
RailSafeDirection = driver.find_element(By.XPATH, "//input[@id='RailSafe']").get_attribute('value')
RailStop = driver.find_element(By.XPATH, "//input[@id='RailSafe']").get_attribute('value')
TrackHeightSwitch = driver.find_element(By.XPATH, "//input[@id='TrkHeightSw']").get_attribute('value')
TrackUnsafeSpeed = driver.find_element(By.XPATH, "//input[@id='TrkUnsafe']").get_attribute('value')
TrackCollisionCount = driver.find_element(By.XPATH, "//input[@id='TrackCollCnt']").get_attribute('value')

Track2 = [TrackBumper,BumperGPIO,RailSafeDirection,RailStop,TrackHeightSwitch,TrackUnsafeSpeed,TrackCollisionCount]

TrackBumperT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Bumper']").text
BumperGPIOT = driver.find_element(By.XPATH, "//td[normalize-space()='Bumper GPIO']").text
RailSafeDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='Rail Safe direction']").text
RailStopT = driver.find_element(By.XPATH, "//td[normalize-space()='Rail Stop']").text
TrackHeightSwitchT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Height Switch']").text
TrackUnsafeSpeedT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Unsafe Speed']").text
TrackCollisionCountT = driver.find_element(By.XPATH, "//td[normalize-space()='Track Collision Count']").text


Track2S = [TrackBumperT,BumperGPIOT,RailSafeDirectionT,RailStopT,TrackHeightSwitchT,TrackUnsafeSpeedT,TrackCollisionCountT]

############################################################################################################################ TRACK PAGE 2

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ TRACK PAGE 3

TPBDirection = driver.find_element(By.XPATH, "//input[@id='TPBunsafe']").get_attribute('value')
TPBOn = driver.find_element(By.XPATH, "//input[@id='TPBon']").get_attribute('value')
TPBOtherDevice = driver.find_element(By.XPATH, "//input[@id='TPBotherDN']").get_attribute('value')
TPBSafeDirection = driver.find_element(By.XPATH, "//input[@id='TPBsafe']").get_attribute('value')
TPBUnsafeDistance = driver.find_element(By.XPATH, "//input[@id='TPBsafe']").get_attribute('value')
TPBFreqWhenMoving = driver.find_element(By.XPATH, "//input[@id='TPBfreq']").get_attribute('value')
TPBPort = driver.find_element(By.XPATH, "//input[@id='TrkPBport']").get_attribute('value')

Track3 = [TPBDirection,TPBOn,TPBOtherDevice,TPBSafeDirection,TPBUnsafeDistance,TPBFreqWhenMoving,TPBPort]

TPBDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Direction Unsafe Speed']").text
TPBOnT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB On']").text
TPBOtherDeviceT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Other Device No']").text
TPBSafeDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Safe direction']").text
TPBUnsafeDistanceT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Safe direction']").text
TPBFreqWhenMovingT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Freq when moving']").text
TPBPortT = driver.find_element(By.XPATH, "//td[normalize-space()='TPB Port']").text


Track3S = [TPBDirectionT,TPBOnT,TPBOtherDeviceT,TPBSafeDirectionT,TPBUnsafeDistanceT,TPBFreqWhenMovingT,TPBPortT]

############################################################################################################################ TRACK PAGE 3

driver.find_element(By.XPATH, "//a[normalize-space()='Lens']").click()
driver.implicitly_wait(2)


############################################################################################################################ LENS PAGE 1

SerialLensProtocol = driver.find_element(By.XPATH, "//input[@id='LensProtocol']").get_attribute('value')
LensSerialMode = driver.find_element(By.XPATH, "//input[@id='LensSerMode']").get_attribute('value')
SerialLensExtOption = driver.find_element(By.XPATH, "//input[@id='ExtVal']").get_attribute('value')
LensExRelayBit = driver.find_element(By.XPATH, "//input[@id='LensExtBit']").get_attribute('value')
UseLensIfForIris = driver.find_element(By.XPATH, "//input[@id='LensIfForIris']").get_attribute('value')
ZoomCRCPS = driver.find_element(By.XPATH, "//input[@id='ZoomCRCPS']").get_attribute('value')
SetFocusTimeout = driver.find_element(By.XPATH, "//input[@id='LensSFtimeout']").get_attribute('value')
SetFocusZoomLevel = driver.find_element(By.XPATH, "//input[@id='LensSFlevel']").get_attribute('value')

Lens1 = [SerialLensProtocol,LensSerialMode,SerialLensExtOption,LensExRelayBit,UseLensIfForIris,ZoomCRCPS,SetFocusTimeout,SetFocusZoomLevel]

SerialLensProtocolT = driver.find_element(By.XPATH, "//td[normalize-space()='Serial Lens Protocol']").text
LensSerialModeT = driver.find_element(By.XPATH, "//td[normalize-space()='Lens Serial Mode']").text
SerialLensExtOptionT = driver.find_element(By.XPATH, "//td[normalize-space()='Serial Lens Ext Option']").text
LensExRelayBitT = driver.find_element(By.XPATH, "//td[normalize-space()='Serial Lens Ext Option']").text
UseLensIfForIrisT = driver.find_element(By.XPATH, "//td[normalize-space()='Use Lens IF for Iris']").text
ZoomCRCPST = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom CRCPS Slope']").text
SetFocusTimeoutT = driver.find_element(By.XPATH, "//td[normalize-space()='Set Focus Timeout']").text
SetFocusZoomLevelT = driver.find_element(By.XPATH, "//td[normalize-space()='Set Focus Zoom Level']").text


Lens1S = [SerialLensProtocolT,LensSerialModeT,SerialLensExtOptionT,LensExRelayBitT,UseLensIfForIrisT,ZoomCRCPST,SetFocusTimeoutT,SetFocusZoomLevelT]

############################################################################################################################ LENS PAGE 1

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ LENS PAGE 2

LensFocusDirection = driver.find_element(By.XPATH, "//input[@id='LensFocusDir']").get_attribute('value')
FocusBacklashConstant = driver.find_element(By.XPATH, "//input[@id='FocusBacklash']").get_attribute('value')
FocusHighLimit = driver.find_element(By.XPATH, "//input[@id='FocusHiLimit']").get_attribute('value')
FocusLowLimit = driver.find_element(By.XPATH, "//input[@id='FocusLoLimit']").get_attribute('value')
FocusMaxAcceleration = driver.find_element(By.XPATH, "//input[@id='FocusMaxAcc']").get_attribute('value')
FocusMaxVelocity = driver.find_element(By.XPATH, "//input[@id='FocusMaxVel']").get_attribute('value')
FocusMinAcceleration = driver.find_element(By.XPATH, "//input[@id='FocusMinAcc']").get_attribute('value')
FocusMultiplier = driver.find_element(By.XPATH, "//input[@id='FocusMultFact']").get_attribute('value')
FocusStartPosition = driver.find_element(By.XPATH, "//input[@id='FocusStartPos']").get_attribute('value')

Lens2 = [LensFocusDirection,FocusBacklashConstant,FocusHighLimit,FocusLowLimit,FocusMaxAcceleration,FocusMaxVelocity,FocusMinAcceleration,FocusMultiplier,FocusStartPosition]

LensFocusDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='Lens Focus Direction']").text
FocusBacklashConstantT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Backlash Constant']").text
FocusHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus High Limit']").text
FocusLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Lo Limit']").text
FocusMaxAccelerationT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Max Acceleration']").text
FocusMaxVelocityT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Max Velocity']").text
FocusMinAccelerationT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Min Acceleration']").text
FocusMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Multiplier']").text
FocusStartPositionT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Start Position']").text


Lens2S = [LensFocusDirectionT,FocusBacklashConstantT,FocusHighLimitT,FocusLowLimitT,FocusMaxAccelerationT,FocusMaxVelocityT,FocusMinAccelerationT,FocusMultiplierT,FocusStartPositionT]

############################################################################################################################ LENS PAGE 2

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ LENS PAGE 3

LensIrisDirection = driver.find_element(By.XPATH, "//input[@id='LensIrisDir']").get_attribute('value')
IrisMaxAcceleration = driver.find_element(By.XPATH, "//input[@id='IrisMaxAcc']").get_attribute('value')
IrisMaxVelocity = driver.find_element(By.XPATH, "//input[@id='IrisMaxVel']").get_attribute('value')
IrisMinAcceleration = driver.find_element(By.XPATH, "//input[@id='IrisMinAcc']").get_attribute('value')
IrisMultiplier = driver.find_element(By.XPATH, "//input[@id='IrisMultFact']").get_attribute('value')
IrisStartPosition = driver.find_element(By.XPATH, "//input[@id='IrisStartPos']").get_attribute('value')

Lens3 = [LensIrisDirection,IrisMaxAcceleration,IrisMaxVelocity,IrisMinAcceleration,IrisMultiplier,IrisStartPosition]

LensIrisDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='Lens Iris Direction']").text
IrisMaxAccelerationT = driver.find_element(By.XPATH, "//td[normalize-space()='Iris Max Acceleration']").text
IrisMaxVelocityT = driver.find_element(By.XPATH, "//td[normalize-space()='Iris Max Velocity']").text
IrisMinAccelerationT = driver.find_element(By.XPATH, "//td[normalize-space()='Iris Min Acceleration']").text
IrisMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Iris Multiplier']").text
IrisStartPositionT = driver.find_element(By.XPATH, "//td[normalize-space()='Iris Start Position']").text


Lens3S = [LensIrisDirectionT,IrisMaxAccelerationT,IrisMaxVelocityT,IrisMinAccelerationT,IrisMultiplierT,IrisStartPositionT]

############################################################################################################################ LENS PAGE 3

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ LENS PAGE 4

LocalFocusOffset = driver.find_element(By.XPATH, "//input[@id='LocFocusOffset']").get_attribute('value')
LocalFocusScaling = driver.find_element(By.XPATH, "//input[@id='LocalFocusScal']").get_attribute('value')
LocalFocusTime = driver.find_element(By.XPATH, "//input[@id='LocalFocusTime']").get_attribute('value')
LocalZoomDeadband = driver.find_element(By.XPATH, "//input[@id='LocalZoomDB']").get_attribute('value')
LocalZoomRange = driver.find_element(By.XPATH, "//input[@id='LocalZoomRange']").get_attribute('value')
LocalZoomTime = driver.find_element(By.XPATH, "//input[@id='LocalZoomTime']").get_attribute('value')

Lens4 = [LocalFocusOffset,LocalFocusScaling,LocalFocusTime,LocalZoomDeadband,LocalZoomRange,LocalZoomTime]

LocalFocusOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Focus Offset']").text
LocalFocusScalingT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Focus Scaling']").text
LocalFocusTimeT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Focus Time']").text
LocalZoomDeadbandT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Zoom Deadband']").text
LocalZoomRangeT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Zoom Range']").text
LocalZoomTimeT = driver.find_element(By.XPATH, "//td[normalize-space()='Local Zoom Time']").text


Lens4S = [LocalFocusOffsetT,LocalFocusScalingT,LocalFocusTimeT,LocalZoomDeadbandT,LocalZoomRangeT,LocalZoomTimeT]

############################################################################################################################ LENS PAGE 4

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ LENS PAGE 5

LensZoomDirection = driver.find_element(By.XPATH, "//input[@id='LensZoomDir']").get_attribute('value')
ZoomBacklashConstant = driver.find_element(By.XPATH, "//input[@id='ZoomBacklash']").get_attribute('value')
ZoomHighLimit = driver.find_element(By.XPATH, "//input[@id='ZoomHiLimit']").get_attribute('value')
ZoomLowLimit = driver.find_element(By.XPATH, "//input[@id='ZoomLoLimit']").get_attribute('value')
ZoomMaxAccel = driver.find_element(By.XPATH, "//input[@id='ZoomMaxAcc']").get_attribute('value')
ZoomMaxVelocity = driver.find_element(By.XPATH, "//input[@id='ZoomMaxVel']").get_attribute('value')
ZoomMinAccel = driver.find_element(By.XPATH, "//input[@id='ZoomMinAcc']").get_attribute('value')
ZoomMultiplier = driver.find_element(By.XPATH, "//input[@id='ZoomMultFact']").get_attribute('value')
ZoomStartPosition = driver.find_element(By.XPATH, "//input[@id='ZoomStartPos']").get_attribute('value')

Lens5 = [LensZoomDirection,ZoomBacklashConstant,ZoomHighLimit,ZoomLowLimit,ZoomMaxAccel,ZoomMaxVelocity,ZoomMinAccel,ZoomMultiplier,ZoomStartPosition]

LensZoomDirectionT = driver.find_element(By.XPATH, "//td[normalize-space()='Lens Zoom Direction']").text
ZoomBacklashConstantT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Backlash Constant']").text
ZoomHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom High Limit']").text
ZoomLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Lo Limit']").text
ZoomMaxAccelT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Max Acceleration']").text
ZoomMaxVelocityT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Max Velocity']").text
ZoomMinAccelT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Min Acceleration']").text
ZoomMultiplierT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Multiplier']").text
ZoomStartPositionT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Start Position']").text


Lens5S = [LensZoomDirectionT,ZoomBacklashConstantT,ZoomHighLimitT,ZoomLowLimitT,ZoomMaxAccelT,ZoomMaxVelocityT,ZoomMinAccelT,ZoomMultiplierT,ZoomStartPositionT]

############################################################################################################################ LENS PAGE 5

driver.find_element(By.XPATH, "//a[normalize-space()='Robot']").click()
driver.implicitly_wait(2)

############################################################################################################################ ROBOT PAGE 1

XReverse = driver.find_element(By.XPATH, "//input[@id='XReverse']").get_attribute('value')
XHighLimit = driver.find_element(By.XPATH, "//input[@id='XHiLimit']").get_attribute('value')
XLowLimit = driver.find_element(By.XPATH, "//input[@id='XLoLimit']").get_attribute('value')
XJsMedium = driver.find_element(By.XPATH, "//input[@id='XMedium']").get_attribute('value')
XJsFine = driver.find_element(By.XPATH, "//input[@id='XFine']").get_attribute('value')
YReverse = driver.find_element(By.XPATH, "//input[@id='YReverse']").get_attribute('value')
YHighLimit = driver.find_element(By.XPATH, "//input[@id='YHiLimit']").get_attribute('value')
YLowLimit = driver.find_element(By.XPATH, "//input[@id='YLoLimit']").get_attribute('value')
YJsMedium = driver.find_element(By.XPATH, "//input[@id='YMedium']").get_attribute('value')
YJsFine = driver.find_element(By.XPATH, "//input[@id='YFine']").get_attribute('value')

Robot1 = [XReverse,XHighLimit,XLowLimit,XJsMedium,XJsFine,YReverse,YHighLimit,YLowLimit,YJsMedium,YJsFine]

XReverseT = driver.find_element(By.XPATH, "//td[normalize-space()='X Reverse']").text
XHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='X High Limit']").text
XLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='X Low Limit']").text
XJsMediumT = driver.find_element(By.XPATH, "//td[normalize-space()='X JS Medium']").text
XJsFineT = driver.find_element(By.XPATH, "//td[normalize-space()='X JS Fine']").text
YReverseT = driver.find_element(By.XPATH, "//td[normalize-space()='Y Reverse']").text
YHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Y High Limit']").text
YLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Y Low Limit']").text
YJsMediumT = driver.find_element(By.XPATH, "//td[normalize-space()='Y JS Medium']").text
YJsFineT = driver.find_element(By.XPATH, "//td[normalize-space()='Y JS Fine']").text


Robot1S = [XReverseT,XHighLimitT,XLowLimitT,XJsMediumT,XJsFineT,YReverseT,YHighLimitT,YLowLimitT,YJsMediumT,YJsFineT]


############################################################################################################################ ROBOT PAGE 1

driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

############################################################################################################################ ROBOT PAGE 2

DerivTimeR = driver.find_element(By.XPATH, "//input[@id='DriveDT']").get_attribute('value')
VelocityFeedForwardR = driver.find_element(By.XPATH, "//input[@id='DriveKVFF']").get_attribute('value')
IntegrationLimitR = driver.find_element(By.XPATH, "//input[@id='DriveIL']").get_attribute('value')
AccelFeedForwardR = driver.find_element(By.XPATH, "//input[@id='DriveKAFF']").get_attribute('value')
KDR = driver.find_element(By.XPATH, "//input[@id='DriveKD']").get_attribute('value')
KIR = driver.find_element(By.XPATH, "//input[@id='DriveKI']").get_attribute('value')
KPR = driver.find_element(By.XPATH, "//input[@id='DriveKP']").get_attribute('value')
MaximumAccelR = driver.find_element(By.XPATH, "//input[@id='DriveMaxAcc']").get_attribute('value')
MaximumVelR = driver.find_element(By.XPATH, "//input[@id='DriveMaxVel']").get_attribute('value')
MinimumAccelR = driver.find_element(By.XPATH, "//input[@id='DriveMinAcc']").get_attribute('value')

Robot2 = [DerivTimeR,VelocityFeedForwardR,AccelFeedForwardR,KDR,KIR,KPR,MaximumAccelR,MaximumVelR,MinimumAccelR]

DerivTimeRT = driver.find_element(By.XPATH, "//td[normalize-space()='Derivative Time']").text
VelocityFeedForwardRT = driver.find_element(By.XPATH, "//td[normalize-space()='Velocity Feed Forward']").text
IntegrationLimitRT = driver.find_element(By.XPATH, "//td[normalize-space()='Integration Limit']").text
AccelFeedForwardRT = driver.find_element(By.XPATH, "//td[normalize-space()='Accel Feed Forward']").text
KDRT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KD']").text
KIRT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KI']").text
KPRT = driver.find_element(By.XPATH, "//td[normalize-space()='PID Loop KP']").text
MaximumAccelRT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Acceleration']").text
MaximumVelRT = driver.find_element(By.XPATH, "//td[normalize-space()='Maximum Velocity']").text
MinimumAccelRT = driver.find_element(By.XPATH, "//td[normalize-space()='Minimum Acceleration']").text


Robot2S = [DerivTimeRT,VelocityFeedForwardRT,AccelFeedForwardRT,KDRT,KIRT,KPRT,MaximumAccelRT,MaximumVelRT,MinimumAccelRT]

############################################################################################################################ ROBOT PAGE 2

driver.find_element(By.XPATH, "//a[normalize-space()='CIU']").click()
driver.implicitly_wait(4)

############################################################################################################################ CIU PAGE 1


CiuMode = driver.find_element(By.XPATH, "//input[@id='CCUmode']").get_attribute('value')
CiuPoll = driver.find_element(By.XPATH, "//input[@id='CCUpoll']").get_attribute('value')
CiuReady = driver.find_element(By.XPATH, "//input[@id='CCUready']").get_attribute('value')
CameraId = driver.find_element(By.XPATH, "//input[@id='CIUcamID']").get_attribute('value')
IpAddressC = driver.find_element(By.XPATH, "//input[@id='CIUaddrIP']").get_attribute('value')
CiuLevelsMask = driver.find_element(By.XPATH, "//input[@id='CIUlevels']").get_attribute('value')
CiuSwitchesMask = driver.find_element(By.XPATH, "//input[@id='CIUswitches']").get_attribute('value')
CIuPortNumber = driver.find_element(By.XPATH, "//input[@id='CIUport']").get_attribute('value')

CIU =[CiuMode,CiuPoll,CiuReady,CameraId,IpAddressC,CiuLevelsMask,CiuSwitchesMask,CIuPortNumber]

CiuModeT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Mode']").text
CiuPollT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Poll (Switches)']").text
CiuReadyT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Ready Indicator']").text
CameraIdT = driver.find_element(By.XPATH, "//td[normalize-space()='Camera ID']").text
IpAddressCT = driver.find_element(By.XPATH, "//td[normalize-space()='IP Address']").text
CiuLevelsMaskT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Levels Mask']").text
CiuSwitchesMaskT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Switches Mask']").text
CIuPortNumberT = driver.find_element(By.XPATH, "//td[normalize-space()='CIU Port Number']").text


CIUS =[CiuModeT,CiuPollT,CiuReadyT,CameraIdT,IpAddressCT,CiuLevelsMaskT,CiuSwitchesMaskT,CIuPortNumberT]

############################################################################################################################ CIU PAGE 1

driver.find_element(By.XPATH, "//a[normalize-space()='Limits']").click()
driver.implicitly_wait(2)

############################################################################################################################ LIMITS PAGE 1

PanHighLimit = driver.find_element(By.XPATH, "//input[@id='PanHiLimit']").get_attribute('value')
PanLowLimit = driver.find_element(By.XPATH, "//input[@id='PanLoLimit']").get_attribute('value')
TiltHighLimit = driver.find_element(By.XPATH, "//input[@id='TiltHiLimit']").get_attribute('value')
TiltLowLimit = driver.find_element(By.XPATH, "//input[@id='TiltLoLimit']").get_attribute('value')
HeightHighLimit = driver.find_element(By.XPATH, "//input[@id='HeightHiLimit']").get_attribute('value')
HeightLowLimit = driver.find_element(By.XPATH, "//input[@id='HeightLoLimit']").get_attribute('value')
FocusHighLimit = driver.find_element(By.XPATH, "//input[@id='FocusHiLimit']").get_attribute('value')
FocusLowLimit = driver.find_element(By.XPATH, "//input[@id='FocusHiLimit']").get_attribute('value')
ZoomHighLimit = driver.find_element(By.XPATH, "//input[@id='ZoomHiLimit']").get_attribute('value')
ZoomLowLimit = driver.find_element(By.XPATH, "//input[@id='ZoomLoLimit']").get_attribute('value')

Limits =[PanHighLimit,PanLowLimit,TiltHighLimit,TiltLowLimit,HeightHighLimit,HeightLowLimit,FocusHighLimit,FocusLowLimit,ZoomHighLimit,ZoomLowLimit]

PanHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan High Limit']").text
PanLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Pan Low Limit']").text
TiltHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt High Limit']").text
TiltLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Tilt Low Limit']").text
HeightHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Height High Limit']").text
HeightLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Height Low Limit']").text
FocusHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus High Limit']").text
FocusLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Focus Low Limit']").text
ZoomHighLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom High Limit']").text
ZoomLowLimitT = driver.find_element(By.XPATH, "//td[normalize-space()='Zoom Low Limit']").text


LimitsS =[PanHighLimitT,PanLowLimitT,TiltHighLimitT,TiltLowLimitT,HeightHighLimitT,HeightLowLimitT,FocusHighLimitT,FocusLowLimitT,ZoomHighLimitT,ZoomLowLimitT]

############################################################################################################################ LIMITS PAGE 1

driver.find_element(By.XPATH, "//a[normalize-space()='VR']").click()
driver.implicitly_wait(2)

############################################################################################################################ VR PAGE 1


VRDataProtocol = driver.find_element(By.XPATH, "//input[@id='VRProtocol']").get_attribute('value')
VRDataBaudRate = driver.find_element(By.XPATH, "//input[@id='VRBaud']").get_attribute('value')
VRPanEncoderRange = driver.find_element(By.XPATH, "//input[@id='VRRangeP']").get_attribute('value')
VRPanInvert = driver.find_element(By.XPATH, "//input[@id='VRInvertP']").get_attribute('value')
VRPanOffset = driver.find_element(By.XPATH, "//input[@id='VROffsetP']").get_attribute('value')
VRTiltEncoderRange = driver.find_element(By.XPATH, "//input[@id='VRRangeT']").get_attribute('value')
VRTiltInvert = driver.find_element(By.XPATH, "//input[@id='VRInvertT']").get_attribute('value')
VRTiltOffset = driver.find_element(By.XPATH, "//input[@id='VROffsetT']").get_attribute('value')
VRHeightEncoderRange = driver.find_element(By.XPATH, "//input[@id='VRRangeH']").get_attribute('value')
VRHeightInvert = driver.find_element(By.XPATH, "//input[@id='VRInvertH']").get_attribute('value')
VRHeightOffset = driver.find_element(By.XPATH, "//input[@id='VROffsetH']").get_attribute('value')
VRHeightTotalMovement = driver.find_element(By.XPATH, "//input[@id='VRTotalH']").get_attribute('value')

VR1 = [VRDataProtocol,VRDataBaudRate,VRPanEncoderRange,VRPanInvert,VRPanOffset,VRTiltEncoderRange,VRTiltInvert,VRTiltOffset,VRHeightEncoderRange,VRHeightInvert,VRHeightOffset,VRHeightTotalMovement]

VRDataProtocolT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Data Protocol']").text
VRDataBaudRateT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Data Baud Rate']").text
VRPanEncoderRangeT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Pan Encoder Range']").text
VRPanInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Pan Invert']").text
VRPanOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Pan Offset']").text
VRTiltEncoderRangeT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Tilt Encoder Range']").text
VRTiltInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Tilt Invert']").text
VRTiltOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Tilt Offset']").text
VRHeightEncoderRangeT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Height Encoder Range']").text
VRHeightInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Height Invert']").text
VRHeightOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Height Offset']").text
VRHeightTotalMovementT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Height Total Movement']").text


VR1S = [VRDataProtocolT,VRDataBaudRateT,VRPanEncoderRangeT,VRPanInvertT,VRPanOffsetT,VRTiltEncoderRangeT,VRTiltInvertT,VRTiltOffsetT,VRHeightEncoderRangeT,VRHeightInvertT,VRHeightOffsetT,VRHeightTotalMovementT]

############################################################################################################################ VR PAGE 1

driver.find_element(By.XPATH, "//input[@id='Nxt']").click()
driver.implicitly_wait(2)

############################################################################################################################ VR PAGE 2

VRFocusInvert = driver.find_element(By.XPATH, "//input[@id='VRInvertF']").get_attribute('value')
VRFocusOffset = driver.find_element(By.XPATH, "//input[@id='VROffsetF']").get_attribute('value')
VRFocusScaling = driver.find_element(By.XPATH, "//input[@id='VRScaleF']").get_attribute('value')
VRZoomInvert = driver.find_element(By.XPATH, "//input[@id='VRInvertZ']").get_attribute('value')
VRZoomLensCalibration = driver.find_element(By.XPATH, "//input[@id='VRLensCalZ']").get_attribute('value')
VRZoomOffset = driver.find_element(By.XPATH, "//input[@id='VROffsetZ']").get_attribute('value')
VRZoomScaling = driver.find_element(By.XPATH, "//input[@id='VRScaleZ']").get_attribute('value')

VR2 = [VRFocusInvert,VRFocusOffset,VRFocusScaling,VRZoomInvert,VRZoomLensCalibration,VRZoomOffset,VRZoomScaling]

VRFocusInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Focus Invert']").text
VRFocusOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Focus Offset']").text
VRFocusScalingT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Focus Scaling']").text
VRZoomInvertT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Invert']").text
VRZoomLensCalibrationT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Lens Calibration']").text
VRZoomOffsetT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Offset']").text
VRZoomScalingT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Scaling']").text


VR2S= [VRFocusInvertT,VRFocusOffsetT,VRFocusScalingT,VRZoomInvertT,VRZoomLensCalibrationT,VRZoomOffsetT,VRZoomScalingT]

############################################################################################################################ VR PAGE 2

driver.find_element(By.XPATH, "//input[@id='Adv']").click()
driver.implicitly_wait(2)

############################################################################################################################ VR PAGE 3

VRZoomCoefQA = driver.find_element(By.XPATH, "//input[@id='VRZoomQA']").get_attribute('value')
VRZoomCoefQB = driver.find_element(By.XPATH, "//input[@id='VRZoomQB']").get_attribute('value')
VRZoomCoefQC = driver.find_element(By.XPATH, "//input[@id='VRZoomQC']").get_attribute('value')
VRZoomScaleFactorQS = driver.find_element(By.XPATH, "//input[@id='VRZoomQS']").get_attribute('value')

VR3 = [VRZoomCoefQA,VRZoomCoefQB,VRZoomCoefQC,VRZoomScaleFactorQS]

VRZoomCoefQAT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Coefficient QA']").text
VRZoomCoefQBT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Coefficient QB']").text
VRZoomCoefQCT = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Coefficient QC']").text
VRZoomScaleFactorQST = driver.find_element(By.XPATH, "//td[normalize-space()='VR Zoom Scale Factor QS']").text


VR3S = [VRZoomCoefQAT,VRZoomCoefQBT,VRZoomCoefQCT,VRZoomScaleFactorQST]

############################################################################################################################ VR PAGE 3


for i in range(0, len(General1S)):
    GeneralPageV.append(General1S[i])
for i in range(0,len(General2S)):
    GeneralPageV.append(General2S[i])
for i in range(0,len(General3S)):
    GeneralPageV.append(General3S[i])
for i in range(0,len(General4S)):
    GeneralPageV.append(General4S[i])
for i in range(0,len(General5S)):
    GeneralPageV.append(General5S[i])
for i in range(0, len(Network1S)):
    NetworkPageV.append(Network1S[i])
for i in range(0,len(Network2S)):
    GeneralPageV.append(Network2S[i])
for i in range(0,len(Network3S)):
    NetworkPageV.append(Network3S[i])
for i in range(0, len(Pan1S)):
    PanPageV.append(Pan1S[i])
for i in range(0,len(Pan2S)):
    PanPageV.append(Pan2S[i])
for i in range(0, len(Tilt1S)):
    TiltPageV.append(Tilt1S[i])
for i in range(0,len(Tilt2S)):
    TiltPageV.append(Tilt2S[i])
for i in range(0, len(Height1S)):
    HeightPageV.append(Height1S[i])
for i in range(0,len(Height2S)):
    HeightPageV.append(Height2S[i])
for i in range(0, len(Track1S)):
    TrackPageV.append(Track1S[i])
for i in range(0,len(Track2S)):
    TrackPageV.append(Track2S[i])
for i in range(0,len(Track3S)):
    TrackPageV.append(Track3S[i])
for i in range(0, len(Lens1S)):
    LensPageV.append(Lens1S[i])
for i in range(0,len(Lens2S)):
    LensPageV.append(Lens2S[i])
for i in range(0,len(Lens3S)):
    LensPageV.append(Lens3S[i])
for i in range(0,len(Lens4S)):
    LensPageV.append(Lens4S[i])
for i in range(0,len(Lens5S)):
    LensPageV.append(Lens5S[i])
for i in range(0, len(Robot1S)):
    RobotPageV.append(Robot1S[i])
for i in range(0,len(Robot2S)):
    RobotPageV.append(Robot2S[i])
for i in range(0, len(VR1S)):
    VRPageV.append(VR1S[i])
for i in range(0,len(VR2S)):
    VRPageV.append(VR2S[i])
for i in range(0,len(VR3S)):
    VRPageV.append(VR3S[i])







for i in range(0, len(General1)):
    GeneralPage.append(General1[i])
for i in range(0,len(General2)):
    GeneralPage.append(General2[i])
for i in range(0,len(General3)):
    GeneralPage.append(General3[i])
for i in range(0,len(General4)):
    GeneralPage.append(General4[i])
for i in range(0,len(General5)):
    GeneralPage.append(General5[i])
for i in range(0, len(Network1)):
    NetworkPage.append(Network1[i])
for i in range(0,len(Network2)):
    GeneralPage.append(Network2[i])
for i in range(0,len(Network3)):
    NetworkPage.append(Network3[i])
for i in range(0, len(Pan1)):
    PanPage.append(Pan1[i])
for i in range(0,len(Pan2)):
    PanPage.append(Pan2[i])
for i in range(0, len(Tilt1)):
    TiltPage.append(Tilt1[i])
for i in range(0,len(Tilt2)):
    TiltPage.append(Tilt2[i])
for i in range(0, len(Height1)):
    HeightPage.append(Height1[i])
for i in range(0,len(Height2)):
    HeightPage.append(Height2[i])
for i in range(0, len(Track1)):
    TrackPage.append(Track1[i])
for i in range(0,len(Track2)):
    TrackPage.append(Track2[i])
for i in range(0,len(Track3)):
    TrackPage.append(Track3[i])
for i in range(0, len(Lens1)):
    LensPage.append(Lens1[i])
for i in range(0,len(Lens2)):
    LensPage.append(Lens2[i])
for i in range(0,len(Lens3)):
    LensPage.append(Lens3[i])
for i in range(0,len(Lens4)):
    LensPage.append(Lens4[i])
for i in range(0,len(Lens5)):
    LensPage.append(Lens5[i])
for i in range(0, len(Robot1)):
    RobotPage.append(Robot1[i])
for i in range(0,len(Robot2)):
    RobotPage.append(Robot2[i])
for i in range(0, len(VR1)):
    VRPage.append(VR1[i])
for i in range(0,len(VR2)):
    VRPage.append(VR2[i])
for i in range(0,len(VR3)):
    VRPage.append(VR3[i])




# print(GeneralPageV)
# print(GeneralPage,"\n","\n")
#
# print(NetworkPageV)
# print(NetworkPage,"\n","\n")
#
# print(PanPageV)
# print(PanPage,"\n","\n")
#
# print(TiltPageV)
# print(TiltPage,"\n","\n")
#
# print(HeightPageV)
# print(HeightPage,"\n","\n")
#
# print(TrackPageV)
# print(TrackPage,"\n","\n")
#
# print(LensPageV)
# print(LensPage,"\n","\n")
#
# print(RobotPageV)
# print(RobotPage,"\n","\n")
#
# print(CIUS)
# print(LimitsS,"\n","\n")
#
# print(VRPageV)
# print(VRPage,"\n","\n")


settings_names2 = GeneralPageV+NetworkPageV+PanPageV+TiltPageV+HeightPageV+TrackPageV+LensPageV+RobotPageV+CIUS+VRPageV
settings_values2 = GeneralPage+NetworkPage+PanPage+TiltPage+HeightPage+TrackPage+LensPage+RobotPage+CIU+VRPage




################################################################################### CMC V2 DATA
print("CMC V2")
for i in range(0,len(settings_names2)):
    print(settings_names2[i],"\n",settings_values2[i])


#################################################################################### CMC V2 DATA
print("\n")

#################################################################################### CMC V1 DATA
print("CMC V1")
for i in range(0,len(settings_names)):
    print(settings_names[i],"\n",settings_values[i])



# print(len(variable_name+variable_nameP)) # print all CMC V1 settings
# settings_names = variable_name+variable_nameP
# settings_values = variable_values+variable_valuesP

# print(len(settings_names),len(settings_values)) # ----------- cmc v1
# print(len(settings_names2),len(settings_values2)) #----------- cmc v2

#################################################################################### CMC V1 DATA


# for i in range(0,len(settings_names2)):
#     x = settings_names2[i]
#     if x in settings_names:
#         print(f"{x} is in CMC V1")
#     else:
#         print("not in the list")




driver.close()








