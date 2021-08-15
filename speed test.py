from remove_whitespace import remove_whitespace
import cv2
import time

input_image = cv2.imread(".//output//74_stitched.png")
time_taken = []
start_time = time.time()

cv2.imwrite("500.png",remove_whitespace(input_image, 500))
time_taken.append(time.time() - start_time)

cv2.imwrite("100.png",remove_whitespace(input_image, 100))
time_taken.append(time.time() - start_time)

cv2.imwrite("50.png",remove_whitespace(input_image, 50))
time_taken.append(time.time() - start_time)

cv2.imwrite("20.png",remove_whitespace(input_image, 20))
time_taken.append(time.time() - start_time)

cv2.imwrite("10.png",remove_whitespace(input_image, 10))
time_taken.append(time.time() - start_time)

cv2.imwrite("5.png",remove_whitespace(input_image, 5))
time_taken.append(time.time() - start_time)

print(f"\n\ntolerance\ttime taken")
print(f"500\t{time_taken[0]}")
print(f"100\t{time_taken[1]}")
print(f"50\t{}time_taken[2]}")
print(f"20\t{}time_taken[3]}")
print(f"10\t{}time_taken[4]}")
print(f"5\t{time_taken[5]}")