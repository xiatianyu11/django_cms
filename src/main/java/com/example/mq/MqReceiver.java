package com.example.mq;

import com.ibm.mq.jms.MQConnectionFactory;
import com.ibm.msg.client.wmq.compat.jms.internal.JMSC;

import javax.jms.*;

public class MqReceiver {

    public static void main(String[] args) {
        try {
            // 创建连接工厂
            MQConnectionFactory factory = new MQConnectionFactory();
            factory.setHostName("localhost");
            factory.setPort(1414);
            factory.setQueueManager("QM1");
            factory.setChannel("DEV.APP.SVRCONN");
            factory.setTransportType(JMSC.MQJMS_TP_CLIENT_MQ_TCPIP);

            // 创建连接
            Connection connection = factory.createConnection();
            connection.start();

            // 创建会话
            Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

            // 创建目标队列
            Queue queue = session.createQueue("DEV.QUEUE.1");

            // 创建消费者
            MessageConsumer consumer = session.createConsumer(queue);

            // 接收消息
            Message message = consumer.receive(1000); // 1000ms超时
            if (message instanceof TextMessage) {
                String text = ((TextMessage) message).getText();
                System.out.println("接收到的消息：" + text);
            }

            // 关闭连接
            consumer.close();
            session.close();
            connection.close();

        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
