package com.example.mq;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.jms.*;

@RestController
public class MqSender {

    @Autowired
    private QueueConnectionFactory connectionFactory;

    @GetMapping("/send")
    public String sendMessage(@RequestParam String message) {
        try (QueueConnection connection = connectionFactory.createQueueConnection("app", "passw0rd")) {
            QueueSession session = connection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
            Queue queue = session.createQueue("DEV.QUEUE.1");
            QueueSender sender = session.createSender(queue);
            TextMessage textMessage = session.createTextMessage(message);
            sender.send(textMessage);
            return "Message sent successfully!";
        } catch (Exception e) {
            e.printStackTrace();
            return "Failed to send message: " + e.getMessage();
        }
    }
}
