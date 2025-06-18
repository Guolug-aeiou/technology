-- MySQL dump 10.13  Distrib 9.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: technology
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `technology`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `technology` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `technology`;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `user_id` int NOT NULL,
  `views` int DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `tag` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_id_to_user_id` (`user_id`),
  CONSTRAINT `questions_id_to_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (61,'如何优化Python代码性能？','我在处理大数据集时遇到性能asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧题，有什么优asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧技巧吗？',66,150,'2025-05-22 15:31:50','test'),(62,'React和Vue哪个更适合大型项目？','我们公司要启动一个新项asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧在技术选asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧型上犹豫不决',54,200,'2025-05-22 15:31:50',NULL),(63,'机器学习模型部署的最佳实践是什么？','从开发到生产环境部asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧有哪些注意事项？',54,180,'2025-05-22 15:31:50',NULL),(64,'如何设计高可用的微服务架构？','需要设计一个电商平台的微服务架构',54,250,'2025-05-22 15:31:50',NULL),(65,'Docker容器网络配置问题','容器间通信遇到困难，asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧何正确配置网络？',54,120,'2025-05-22 15:31:50','python'),(66,'区块链智能合约安全性问题','如何确保智asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧合约没有漏洞？',54,190,'2025-05-22 15:31:50','python'),(67,'Kubernetes集群自动扩展方案','如何根asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧负载自动扩展K8s集群？',54,210,'2025-05-22 15:31:50','android'),(68,'前端性能优化技巧','有哪些实用的asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧前端性能优化方法？',54,160,'2025-05-22 15:31:50','android'),(69,'MySQL索引优化策略','大数据量asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧如何设计高效索引？',54,230,'2025-05-22 15:31:50','android'),(70,'REST API设计规范','设计REST API时有哪些最佳实践？',54,170,'2025-05-22 15:31:50','python'),(71,'Android应用内存泄漏排查','如何定位和解决Android内存泄漏？',54,140,'2025-05-22 15:31:50','android'),(72,'Python异步编程最佳实践','asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧asyncio在实际项目中的应用技巧',54,180,'2025-05-22 15:31:50','python'),(73,'Java垃圾回收调优','如何优化JVM垃圾回收性能？',54,200,'2025-05-22 15:31:50','python'),(74,'Web安全防护措施','防范XSS和CSRF攻击的有效方法',54,220,'2025-05-22 15:31:50','python'),(75,'AWS架构设计原则','在AWS上设计高可用架构的要点',55,241,'2025-05-22 15:31:50','python'),(76,'Flask和Django如何选择？','中小型项目应该选择哪个框架？',56,130,'2025-05-22 15:31:50','python'),(77,'大数据处理技术选型','Hadoop vs Spark vs Flink比较11111111111111111',52,190,'2025-05-22 15:31:50','pythonandroid'),(78,'CI/CD流水线设计222','3333333333333333',57,210,'2025-05-22 15:31:50','python2222222222222'),(79,'NoSQL数据库适用场景','333333333333333333333333333333333333333333333333333333333333333333333333',57,160,'2025-05-22 15:31:50','android'),(80,'物联网安全防护','12222222222222222222222222222222222222222222222222222222222222222222222222222',57,181,'2025-05-22 15:31:50','android'),(86,'异步函数设计原则','避免阻塞操作：在异步函数中禁止使用time.sleep()、requests.get()等同步阻塞函数，改用asyncio.sleep()、aiohttp.ClientSession等异步替代方案。\r\n保持函数纯粹异步：若部分逻辑必须使用同步代码，可通过asyncio.to_thread()将其放入线程池中执行，避免阻塞事件循环。',57,0,'2025-05-31 20:42:13',NULL),(87,'Python异步编程最佳实践','1. 异步函数设计原则\n- **避免阻塞操作**：在异步函数中禁止使用`time.sleep()`、`requests.get()`等同步阻塞函数，改用`asyncio.sleep()`、`aiohttp.ClientSession`等异步替代方案。\n- **保持函数纯粹异步**：若部分逻辑必须使用同步代码，可通过`asyncio.to_thread()`将其放入线程池中执行，避免阻塞事件循环。\n```python\n# 错误示例\nasync def fetch_data():\n    time.sleep(1)  # 阻塞事件循环\n    return requests.get(url)\n\n# 正确示例\nasync def fetch_data():\n    await asyncio.sleep(1)  # 非阻塞延迟\n    async with aiohttp.ClientSession() as session:\n        return await session.get(url)\n```\n\n2. 任务并发与控制\n- **批量并发**：使用`asyncio.gather()`一次性并发多个任务，支持结果聚合和异常传播。\n- **限流与信号量**：通过`asyncio.Semaphore`限制同时运行的任务数量，防止资源耗尽。\n```python\n# 限制并发数为5\nsemaphore = asyncio.Semaphore(5)\n\nasync def worker(task_id):\n    async with semaphore:\n        await process_task(task_id)\n\n# 并发执行100个任务，但限制同时运行数为5\nawait asyncio.gather(*[worker(i) for i in range(100)])\n```\n\n3. 错误处理与超时机制\n- **全局异常捕获**：在主协程中使用`try-except`捕获所有子任务抛出的异常，避免单个任务失败导致整个程序崩溃。\n- **细粒度超时控制**：为每个任务单独设置超时，避免长时间阻塞。\n```python\nasync def main():\n    tasks = [asyncio.create_task(fetch_data(url)) for url in urls]\n    try:\n        # 全局超时控制\n        results = await asyncio.gather(*tasks, timeout=10)\n    except asyncio.TimeoutError:\n        print(\"部分任务超时\")\n    except Exception as e:\n        print(f\"发生未知错误: {e}\")\n```\n\n4. 资源管理与清理\n- **异步上下文管理器**：使用`async with`语法管理资源（如数据库连接、文件句柄），确保自动释放。\n- **任务取消机制**：通过`task.cancel()`主动取消长时间运行的任务，并在协程内部通过`try-except`处理`CancelledError`。\n```python\nasync def cleanup_task():\n    try:\n        while True:\n            await process_item()\n    except asyncio.CancelledError:\n        await release_resources()  # 清理资源\n        raise\n```\n\n5. 性能优化与调试\n- **避免CPU密集型操作**：异步编程更适合IO密集型任务，对于CPU密集型操作（如大量计算），建议使用`asyncio.to_thread()`或`concurrent.futures.ProcessPoolExecutor`。\n- **调试工具**：使用`asyncio.run(debug=True)`启用调试模式，检测协程泄漏、长时间运行任务等问题。',57,0,'2025-05-31 20:44:49',NULL),(88,'asyncio在实际项目中的应用技巧','1. 异步网络爬虫开发\n- **请求限流**：结合`aiohttp`和`asyncio.Semaphore`控制并发请求数，避免被目标网站封禁。\n- **自动重试**：对失败请求实现指数退避重试机制，提高爬取成功率。\n```python\n# 带指数退避的异步请求\nasync def fetch_with_retry(url, retries=3):\n    for i in range(retries):\n        try:\n            async with session.get(url) as response:\n                return await response.text()\n        except Exception as e:\n            wait_time = 2 ** i  # 指数退避：2s, 4s, 8s...\n            await asyncio.sleep(wait_time)\n```\n\n2. 实时数据流处理\n- **异步队列与背压**：使用`asyncio.Queue`构建生产者-消费者模型，通过队列大小实现背压控制。\n- **批量处理**：消费者端累积一定数量的数据后再批量写入数据库，减少IO次数。\n```python\n# 生产者\nasync def produce(queue):\n    while True:\n        data = await get_data_from_source()\n        await queue.put(data)\n\n# 消费者（每100条数据批量写入）\nasync def consume(queue):\n    batch = []\n    while True:\n        item = await queue.get()\n        batch.append(item)\n        if len(batch) >= 100:\n            await db_batch_insert(batch)\n            batch = []\n```\n\n3. 微服务异步通信\n- **异步RPC客户端**：使用`asyncio`实现基于HTTP/2或gRPC的异步微服务调用。\n- **消息队列集成**：通过`aiokafka`、`aio_pika`等库实现与Kafka、RabbitMQ的异步通信。\n```python\n# 异步Kafka消费者示例\nfrom aiokafka import AIOKafkaConsumer\n\nasync def consume_kafka():\n    consumer = AIOKafkaConsumer(\n        \'my_topic\',\n        bootstrap_servers=\'localhost:9092\',\n        group_id=\'my_group\'\n    )\n    await consumer.start()\n    try:\n        async for msg in consumer:\n            await process_message(msg.value)\n    finally:\n        await consumer.stop()\n```\n\n4. 定时任务调度系统\n- **异步定时任务**：结合`asyncio.create_task()`和`asyncio.sleep()`实现周期性任务。\n- **动态任务管理**：支持运行时添加、删除定时任务，无需重启服务。\n```python\n# 异步定时任务注册中心\nclass Scheduler:\n    def __init__(self):\n        self.tasks = {}\n    \n    async def add_task(self, name, interval, coro):\n        async def periodic():\n            while True:\n                await coro()\n                await asyncio.sleep(interval)\n        \n        task = asyncio.create_task(periodic())\n        self.tasks[name] = task\n    \n    def remove_task(self, name):\n        self.tasks[name].cancel()\n        del self.tasks[name]\n```\n\n5. 数据库异步操作优化\n- **连接池管理**：使用`asyncpg`或`aiomysql`创建异步连接池，复用数据库连接。\n- **事务处理**：通过`async with`语法实现异步事务，确保数据一致性。\n```python\n# 异步PostgreSQL事务示例\nasync with pool.acquire() as connection:\n    async with connection.transaction():\n        await connection.execute(\"INSERT INTO users ...\")\n        await connection.execute(\"UPDATE orders ...\")\n```\n\n6. 高并发WebSocket服务\n- **会话管理**：使用字典维护用户ID到WebSocket连接的映射，支持广播和点对点消息。\n- **心跳机制**：定期发送心跳包检测连接状态，自动断开失效连接。\n```python\n# WebSocket服务示例\nasync def websocket_handler(request):\n    ws = web.WebSocketResponse()\n    await ws.prepare(request)\n    \n    # 注册用户连接\n    user_id = request.query.get(\'user_id\')\n    user_connections[user_id] = ws\n    \n    try:\n        async for msg in ws:\n            if msg.type == web.WSMsgType.TEXT:\n                await process_message(user_id, msg.data)\n    finally:\n        # 清理连接\n        if user_id in user_connections:\n            del user_connections[user_id]\n```',57,0,'2025-05-31 20:44:49',NULL),(89,'test','test',66,0,'2025-06-13 22:43:40',NULL),(160,'admin','admin\r\n',66,0,'2025-06-13 22:56:56',NULL);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (27,'Cloud Computing'),(26,'Cybersecurity'),(29,'Database'),(30,'DevOps'),(23,'Java'),(22,'JavaScript'),(24,'Machine Learning'),(28,'Mobile Development'),(21,'Python'),(25,'Web Development');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(128) NOT NULL,
  `avatar` varchar(200) DEFAULT 'default.jpg',
  `score` int DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (42,'tech_guru','guru@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img2.png',150,'2025-05-22 15:28:11'),(43,'test1','master@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',200,'2025-05-22 15:28:11'),(44,'data_scientist','scientist@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',180,'2025-05-22 15:28:11'),(45,'web_designer','designer@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',90,'2025-05-22 15:28:11'),(46,'ai_researcher','ai@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',250,'2025-05-22 15:28:11'),(47,'devops_engineer','devops@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',120,'2025-05-22 15:28:11'),(48,'cyber_security','security@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',170,'2025-05-22 15:28:11'),(49,'mobile_dev','mobile@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',80,'2025-05-22 15:28:11'),(50,'cloud_architect','cloud@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',210,'2025-05-22 15:28:11'),(51,'blockchain_dev','blockchain@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',190,'2025-05-22 15:28:11'),(52,'game_developer','game@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',70,'2025-05-22 15:28:11'),(53,'python_expert','python@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',220,'2025-05-22 15:28:11'),(54,'java_pro','java@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',160,'2025-05-22 15:28:11'),(55,'frontend_wizard','frontend@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',140,'2025-05-22 15:28:11'),(56,'database_admin','db@example.com','5f4dcc3b5aa765d61d8327deb882cf99','img.png',230,'2025-05-22 15:28:11'),(57,'12','guolug63@gmail.com','1','img2.png',0,'2025-05-22 18:16:12'),(58,'121','123','1234','img4.png',0,'2025-05-22 19:22:13'),(63,'12111','1213','1234','img1.png',0,'2025-05-22 19:24:13'),(64,'test','test@qq.com','test','img3.png',0,'2025-05-26 19:15:41'),(65,'guolug','guolug@126.com','guolug','img5.png',0,'2025-05-31 21:11:01'),(66,'admin','admin@qq.com','admin','img2.png',0,'2025-06-13 22:21:25');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-18 11:39:30
