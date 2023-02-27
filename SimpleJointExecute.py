
import dm_control
from dm_control import mujoco
from dm_control.mujoco.wrapper.mjbindings import enums
from dm_control.mujoco.wrapper.mjbindings import mjlib
from mujoco import viewer

model = mujoco.MjModel.from_xml_path('/Users/shanebarys/BortonLab/SimpleJoint.xml')
data = mujoco.MjData(model)

viewer.launch(model)

# print(sim.model.get_joint_qvel_addr(knee_joint))
print("timestep", data.qpos)