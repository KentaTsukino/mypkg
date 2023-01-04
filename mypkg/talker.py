import rclpy
from rclpy.node import Node
from person_person_msgs.srv import Query


def cb(request, response):
    if request.name == "月野賢汰":
	response.age = 44
    else:
	response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb) 
rclpy.spin(node)
