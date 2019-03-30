## Deploying on PythonAnywhere

1. สมัคร https://www.pythonanywhere.com/
2. ไปที่แท็บ Web เราจะสามารถ configure ตัว Web server ของเราได้
3. ไปที่แท็บ Consoles เพื่อเตรียมเครื่องสำหรับ service ที่เราจะสร้าง เลือก Bash console
4. ตรวจสอบว่าเราอยู่ใน directory ที่เราควรอยู่หรือเปล่า directory ควรจะเป็นประมาณนี้ `/home/zkan/mysite`
5. รันคำสั่งด้านล่างนี้เพื่อติดตั้ง package ที่ใช้เพื่อสร้าง Web server ของเรา (Flask) และ Scikit-Learn

```sh
mkvirtualenv --python=/usr/bin/python3.6 my-virtualenv
workon my-virtualenv
pip install flask scikit-learn
```

6. อัพโหลดไฟล์ที่จำเป็นต้องใช้ขึ้นไปบน server
7. กลับไปที่แท็บ Web เพื่อ configure เครื่อง server ของเราใหม่
  1. แก้ไขส่วนของ Virtualenv
  2. Restart server

## Sending Data

```sh
curl -X POST -H "Content-Type: application/json" -d '{"data": [[3, 5, 4, 2]]}' http://<your_domain>/predict
curl -X POST -H "Content-Type: application/json" -d '{"data": [[3, 5, 4, 2], [5, 4, 3, 2]]}' http://<your_domain>/predict
```