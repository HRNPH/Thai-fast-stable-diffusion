# Thai-Fast-Stable-Diffusion
forked originally from https://github.com/TheLastBen/fast-stable-diffusion

โปรเจ็คเพื่อ **การศึกษาล้วนๆ** ในการเรียนรู้เกี่ยวกับ
- การหาชุดข้อมูลสำหรับ Stable Diffusion
- การ Preprocessing ข้อมูลรูปภาพเบื้องต้น
- การฝึกสอนโมเดล Stable Diffusion

ซึ่งถูกนำมาแปลไทยเพื่อให้เข้าถึงได้ง่ายขึ้นโดยคนไทย อย่างน้อยๆก็ไม่มีกำแพงภาษา
ไม่ต้องไปนั่งกด Midjourny แต่ทำโมเดลในสไตล์ของตัวเองได้เลย


โปรเจ็คนี้โหลด dependencies จาก repo ต้นฉบับมาใช้งานเลย จึงจะอัพเดทตาม repo ต้นฉบับ
หากมีการเปลี่ยนแปลงใน repo ต้นฉบับ เราจะทำการแปลเพิ่มเติมให้เร็วที่สุด

หากมีข้อสงสัยหรือต้องการแก้ไข(ช่วยแปล, แก้) สามารถส่ง PR มาได้เลย
หรือติดต่อผมได้ที่ [Profile](https://www.github.com/hrnph) หากมีเวลาจะมาตอบคำถาม


This is a **totally educational project** to learn about
- Getting dataset for stable diffusion
- Preprocessing the data
- Training Stable Diffusion

Translated to **Thai** to make it easier for Thai people to use

the dependencies was connected to the original repo,
so it'll be up to date

# การใช้งาน
```bash
-- เตรียมโค้ดสำหรับการใช้งาน --
- ทำการดาวน์โหลดโปรเจ็ค (zip หรือ git clone)
- เข้าไปในโฟลเดอร์ แล้วนำไฟล์ .ipynb ไปเปิดใน Google Colab
- ทำการเชื่อมต่อกับ Google Drive ของตัวเอง

-- เตรียมข้อมูลสำหรับการฝึกสอน --
- หาชุดข้อมูลที่ต้องการใช้ แล้วโหลดมาไว้ใน folder /datasets บนเครื่องของตัวเอง
- ทำการแก้ไขชื่อของชุดข้อมูลใน /datasets ให้ตรงกับชื่อที่อยากใช้เป็น Keyword ในโมเดล เช่น kwrd (1).jpg, kwrd (2).jpg
(ใช้ renamer.exe ทำการเปลี่ยนชื่อได้ง่ายๆเลย
)
- upload ขึ้นไปบน Google Drive ของตัวเอง หรือ อัพโหลดผ่านตัว Notebook ได้เลย

-- ฝึกสอนโมเดล --
- ทำตามขั้นตอนใน Notebook ได้เลย
```

# ผู้พัฒนา
<a href="https://github.com/parinzee/charian-diffusion/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=parinzee/charian-diffusion" />
</a>
