FROM openjdk:17-alpine
COPY ApiDemo-0.0.1-SNAPSHOT.jar app.jar
ENV SERVER_PORT=8080
ENTRYPOINT ["java", "-jar", "app.jar"]