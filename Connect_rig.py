from maya import cmds
import pymel.core as pm


cmds.createEmbeddedNodeRL4(
n="rigLogicNode", #name your rig logic node filename here, the node will have the same name

dfp_path="C:\Maya\Journalist\scripts\Kristofer_rl.dna", #enter the path to the file here, no need to change backslash in windows. 
dfp=dfp_path.replace("\\", "/")
jn="DHIhead:<objName>.<attrName>", 
amn="FRM_WMmultipliers.<objName>_<attrName>", 
bsn="<objName>_blendShapes.<attrName>", 
cn="<objName>.<attrName>"
)
