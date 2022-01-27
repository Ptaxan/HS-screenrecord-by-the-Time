from airtest.core.api import *

record_time = 127
dev = connect_device("Android:///")
package_name = "com.playrix.homescapes"

dev.start_recording(max_time=record_time, bit_rate_level=5)
dev.start_app(package_name)
sleep(record_time)
dev.stop_app(package_name)
dev.stop_recording(output="homescapes.mp4")