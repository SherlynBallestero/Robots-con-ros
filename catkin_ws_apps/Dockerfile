# FROM osrf/ros:noetic-desktop-full

# # Instala dependencias adicionales si es necesario
# RUN apt-get update && apt-get install -y \
#     python3-rosdep \
#     python3-rosinstall \
#     python3-rosinstall-generator \
#     python3-wstool \
#     build-essential

# # Eliminar el archivo de lista de fuentes predeterminado de rosdep
# RUN rm -f /etc/ros/rosdep/sources.list.d/20-default.list
# # Configura rosdep
# RUN rosdep init && rosdep update


# Usar la imagen base de ROS Noetic Desktop Full
FROM osrf/ros:noetic-desktop-full

# Instalar paquetes adicionales si es necesario
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential


# Instalar rospy
RUN apt-get update && apt-get install -y \
    ros-noetic-rospy \
    && rm -rf /var/lib/apt/lists/*

# Configurar el entorno de ROS
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Establecer el directorio de trabajo
WORKDIR /root/catkin_ws

# Crear un espacio de trabajo de catkin
RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && \
                  mkdir -p /root/catkin_ws/src && \
                  cd /root/catkin_ws/ && \
                  catkin_make"

# Fuente del entorno de ROS
CMD ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && /bin/bash"]


