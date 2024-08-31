import rospy 


def nodo():
    rospy.init_node('nodo1')
    mensaje="Hola Mundo"
    rospy.loginfo(mensaje)



if __name__=="__main__":
    try: 
        nodo()
    except rospy.ROSInterruptException:
        print("Error")