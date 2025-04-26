docker run -d --name ibm-mq -p 1414:1414 -p 9443:9443 -e LICENSE=accept -e MQ_QMGR_NAME=QM1  icr.io/ibm-messaging/mq:latest

docker exec -ti ibm-mq bash

runmqsc QM1

# 修改认证配置
ALTER QMGR CONNAUTH('')

# 重新加载配置
REFRESH SECURITY TYPE(CONNAUTH)

END