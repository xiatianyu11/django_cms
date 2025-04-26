package com.example.mq;

import com.ibm.mq.jms.MQQueueConnectionFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.jms.JMSException;
import javax.jms.QueueConnectionFactory;

@Configuration
public class MqConfig {

    @Bean
    public QueueConnectionFactory connectionFactory() throws JMSException {
        MQQueueConnectionFactory factory = new MQQueueConnectionFactory();
        factory.setHostName("localhost");
        factory.setPort(1414);
        factory.setQueueManager("QM1");
        factory.setChannel("DEV.APP.SVRCONN");
        factory.setTransportType(1); // MQTransportType.CLIENT
        return factory;
    }
}
