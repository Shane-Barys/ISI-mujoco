
import dm_control
from dm_control import mujoco
from dm_control.mujoco.wrapper.mjbindings import enums
from dm_control.mujoco.wrapper.mjbindings import mjlib
from mujoco import viewer




physics = mujoco.Physics.from_xml_path('/Users/shanebarys/BortonLab/SimpleJoint.xml')
#pixels = physics.render()
model = mujoco.MjModel.from_xml_path('/Users/shanebarys/BortonLab/SimpleJoint.xml')
data = mujoco.MjData(model)

viewer.launch(model)

#tendon_id = model.mj_name2id('tendon', 'hamstring_right')
#tendon_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_TENDON, 'hamstring_right')


with physics.reset_context():
    physics.named.data.qpos['knee_right'] = 0.5

print(physics.named.data.geom_xpos)

print(physics.named.data.geom_xpos[['shin_right', 'thigh_right'], 'z'])
# while physics.time() <5.:
#     physics.step()
#     #print(physics.time())
#     #print(physics.named.data.geom_xpos[['shin_right', 'thigh_right'], 'z'])
while 1==1:
    print(physics.named.data.geom_xpos[['shin_right', 'thigh_right'], 'z'])


print(physics.named.data.geom_xpos[['shin_right', 'thigh_right'], 'z'])
print(model.actuator_lengthrange)


#print(physics.named.data.qpos(['hamstring_right']))
#print(physics.named.data.qpos(model.mjOBJ_tendon['hamstring_right']))
#print(physics.named.data.qpos(tendon_id))


