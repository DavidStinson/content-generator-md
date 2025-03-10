
<table style="width:100%">
  <tr>
    <td colspan="2" style="font-weight: bold;text-align:center;font-size:1.4em">💿 Postgres</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Command</td>
    <td style="font-weight: bold;">Explanation</td>
  </tr>
  <tr>
    <td>sudo service postgresql start</td>
    <td>This command is used to start the PostgreSQL service on your system</td>
  </tr>
  <tr>
    <td>sudo service postgresql stop</td>
    <td>This command is used to stop the PostgreSQL service on your system</td>
  </tr>
</table>

<table style="width:100%">
  <tr>
    <td colspan="2" style="font-weight: bold;text-align:center;font-size:1.4em">🚢 Docker</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Command</td>
    <td style="font-weight: bold;">Explanation</td>
  </tr>
    <tr>
    <td>sudo service docker start</td>
    <td>Similar to the previous command, this one starts the Docker service on your system. Docker must be running to manage containers and images</td>
  </tr>
  <tr>
    <td>sudo docker network create &lt;network_name&gt;</td>
    <td>This Docker command creates a new network (providing the network_name given). Docker networks provide a way for Docker containers to communicate with each other directly and also with the outside world. They can be especially useful in microservices architecture.</td>
  </tr>
  <tr>
    <td>sudo docker network list</td>
    <td>List all networks</td>
  </tr>
  <tr>
    <td>sudo docker network inspect &lt;network_name&gt; </td>
    <td>Display detailed information on one or more networks</td>
  </tr>
  <tr>
    <td>sudo docker ps</td>
    <td>This command lists all currently running Docker containers. It shows details like container ID, image used, when the container was created, the status, ports, and name</td>
  </tr>
  <tr>
    <td>sudo docker ps -a</td>
    <td>This command lists all Docker containers, including those that are currently running and those that have stopped. This is useful for seeing a complete history of containers on your system.</td>
  </tr>
  <tr>
    <td>sudo docker stop &lt;container_id&gt;</td>
    <td>This command will stop the container that is currently running</td>
  </tr>
  <tr>
    <td>sudo docker start &lt;container_id&gt;</td>
    <td>Restarts a previously created and stopped Docker container identified by its container_id.</td>
  </tr>
  <tr>
    <td>sudo docker rm -f &lt;container_id&gt;</td>
    <td>This command forcefully removes a Docker container specified by its container_id. The -f flag stands for force, and it ensures that the container is stopped and then removed</td>
  </tr>
  <tr>
    <td>sudo docker rmi &lt;image_name&gt;</td>
    <td>This command removes a Docker image from your local storage. image_name is the name of the image you want to remove. Images are templates used to create containers and are stored locally once pulled from a registry like Docker Hub.</td>
  </tr>
  <tr>
    <td>sudo docker inspect &lt;image_name&gt;</td>
    <td>This command displays detailed information in JSON format about a Docker image specified by image-name. It includes information like the image's layers, tags, and configuration details.</td>
  </tr>
  <tr>
    <td>sudo docker logs &lt;container_id&gt;</td>
    <td>This command fetches the logs of a Docker container. It's useful for debugging and understanding the behavior of applications running inside containers.</td>
  </tr>
  <tr>
    <td>sudo docker network ls</td>
    <td>Lists all networks created in Docker on your system. This can include default networks like bridge, host, and none, along with any custom networks you've created.</td>
  </tr>
  <tr>
    <td>sudo docker network rm &lt;network_name&gt;</td>
    <td>Removes a Docker network specified by network_name. Containers must be disconnected from the network before it can be removed</td>
  </tr>
  <tr>
    <td>sudo docker image prune --all --force</td>
    <td>Remove all the docker images.</td>
  </tr>

  <tr>
    <td>sudo docker &lt;COMMAND_NAME&gt; --help</td>
    <td>For more information on a command.</td>
  </tr>
  <tr>
    <td>sudo docker exec -it &lt;CONTAINER_NAME&gt; sh</td>
    <td>Opens an interactive shell inside the running Docker container.</td>
  </tr>
</table>

<table style="width:100%">
  <tr>
    <td colspan="2" style="font-weight: bold;text-align:center;font-size:1.4em">🔔 Other Commands</td>
  </tr>
  <tr>
    <td style="font-weight: bold;">Command</td>
    <td style="font-weight: bold;">Explanation</td>
  </tr>
  <tr>
    <td>sudo kill -9 $(sudo lsof -t -i:3000)</td>
    <td>If the port is running it will kill given port number (in this case: 3000), or else throws an error saying not enough arguments.</td>
  </tr>
  <tr>
    <td>/opt/Postman/app/Postman</td>
    <td>Open Postman</td>
  </tr>
</table>
