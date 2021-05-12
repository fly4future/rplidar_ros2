from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            node_name='rplidar_composition',
            package='rplidar_ros2',
            node_executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',
                'serial_baudrate': 256000,
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
            }],
        ),
    ])
