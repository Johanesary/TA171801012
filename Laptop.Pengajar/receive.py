import os
import win32com.client
import json
import pika
import time

#falafel = "ikan"
#contoh = falafel + "ayam"
#credentials = pika.PlainCredentials('kondisiruang', 'kondisiruang')
credentials = pika.PlainCredentials('belva', 'hololens')
parameters = pika.ConnectionParameters('172.20.10.7',
                                       5672,
                                       '/', #kondisiruang
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='Voice',durable=True)

channel.queue_bind(exchange = 'amq.topic', queue = 'Voice', routing_key = 'voice.laptop')
shell = win32com.client.Dispatch("Wscript.Shell")
def callback(ch,method, properties, body):
    print("Received %r" % body)
    if (body == "TUNJUKKAN SLIDE\n"):
        shell.Run("powerpnt TES.pptx")
        time.sleep(5)
        shell.AppActivate("Powerpnt")
        shell.SendKeys("{ENTER}")
        time.sleep(.5)
        shell.SendKeys("{F5}")
        shell.Run("balcon -n Vocalizer Damayanti -f TUNJUKKAN-SLIDE.txt")
    elif (body == "PINDAH SLIDE\n"):
        shell.AppActivate("Powerpnt")
        #time.sleep(.5)
        shell.SendKeys("{RIGHT}")
    elif (body == "TUTUP SLIDE\n"):
        shell.Run("C:\WINDOWS\SYSTEM32\TASKKILL.EXE /F /IM powerpnt.exe")
    elif (body == "BUKA BROWSER\n"):
        shell.Run("chrome")	
    elif (body == "TUTUP BROWSER\n"):
        shell.Run("C:\WINDOWS\SYSTEM32\TASKKILL.EXE /F /IM chrome.exe")
    elif (body == "HALO TITAN\n"):
        shell.Run("balcon -n Vocalizer Damayanti -f HALO-TITAN.txt")
    elif (body == "NYALAKAN MUSIK\n"):
        shell.Run("spotify.vbs")
        shell.Run("balcon -n Vocalizer Damayanti -f NYALAKAN-MUSIK.txt")
    elif (body == "MATIKAN MUSIK\n"):
        shell.Run("C:\WINDOWS\SYSTEM32\TASKKILL.EXE /F /IM Spotify.exe")
        shell.Run("balcon -n Vocalizer Damayanti -f MATIKAN-MUSIK.txt")
    elif (body == "AKTIFKAN SISTEM\n"):
        shell.Run("balcon -n Vocalizer Damayanti -f AKTIFKAN-SISTEM.txt")
    elif (body == "MATIKAN LAMPU\n"): #BERHUBUNGAN DENGAN LAMPU
        shell.Run("balcon -n Vocalizer Damayanti -f MATIKAN-LAMPU.txt")
    elif (body == "NYALAKAN LAMPU\n"):
        shell.Run("balcon -n Vocalizer Damayanti -f NYALAKAN-LAMPU.txt")
    elif (body == "NYALAKAN LAMPU ZONA SATU\n"): #ZONA
         shell.Run("balcon -n Vocalizer Damayanti -f NLZ1.txt")
    elif (body == "NYALAKAN LAMPU ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NLZ2.txt")
    elif (body == "NYALAKAN LAMPU ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NLZ3.txt")
    elif (body == "NYALAKAN LAMPU ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NLZ4.txt")
    elif (body == "TERANGKAN LAMPU MENJADI SEPULUH PERSEN\n"): #TERANGKAN
         shell.Run("balcon -n Vocalizer Damayanti -f TL10.txt")
    elif (body == "TERANGKAN LAMPU MENJADI DUA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL20.txt")
    elif (body == "TERANGKAN LAMPU MENJADI TIGA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL30.txt")
    elif (body == "TERANGKAN LAMPU MENJADI EMPAT PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL40.txt")
    elif (body == "TERANGKAN LAMPU MENJADI LIMA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL50.txt")
    elif (body == "TERANGKAN LAMPU MENJADI ENAM PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL60.txt")
    elif (body == "TERANGKAN LAMPU MENJADI TUJUH PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL70.txt")
    elif (body == "TERANGKAN LAMPU MENJADI DELAPAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL80.txt")
    elif (body == "TERANGKAN LAMPU MENJADI SEMBILAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL90.txt")
    elif (body == "TERANGKAN LAMPU MENJADI SERATUS PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TL100.txt")
    elif (body == "REDUPKAN LAMPU MENJADI SEPULUH PERSEN\n"): #REDUPKAN
         shell.Run("balcon -n Vocalizer Damayanti -f RL10.txt")
    elif (body == "REDUPKAN LAMPU MENJADI DUA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL20.txt")
    elif (body == "REDUPKAN LAMPU MENJADI TIGA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL30.txt")
    elif (body == "REDUPKAN LAMPU MENJADI EMPAT PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL40.txt")
    elif (body == "REDUPKAN LAMPU MENJADI LIMA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL50.txt")
    elif (body == "REDUPKAN LAMPU MENJADI ENAM PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL60.txt")
    elif (body == "REDUPKAN LAMPU MENJADI TUJUH PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL70.txt")
    elif (body == "REDUPKAN LAMPU MENJADI DELAPAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL80.txt")
    elif (body == "REDUPKAN LAMPU MENJADI SEMBILAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f RL90.txt")
    elif (body == "BERAPA INTENSITAS CAHAYA SAAT INI\n"): #INTENSITAS CAHAYA
         shell.Run("balcon -n Vocalizer Damayanti -f INTENC.txt")
    elif (body == "BERAPA INTENSITAS CAHAYA ZONA SATU SAAT INI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f INTENZ1.txt")
    elif (body == "BERAPA INTENSITAS CAHAYA ZONA DUA SAAT INI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f INTENZ2.txt")
    elif (body == "BERAPA INTENSITAS CAHAYA ZONA TIGA SAAT INI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f INTENZ3.txt")
    elif (body == "BERAPA INTENSITAS CAHAYA ZONA EMPAT SAAT INI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f INTENZ4.txt")
    elif ((body == "BERAPA SUHU UDARA SAAT INI\n") or (body == "TUNJUKKAN SUHU\n") ):
         shell.Run("balcon -n Vocalizer Damayanti -f SUHU.txt")
    elif ((body == "BERAPA SUHU UDARA ZONA SATU SAAT INI\n")  or (body == "TUNJUKKAN SUHU ZONA SATU\n") ):
         shell.Run("balcon -n Vocalizer Damayanti -f SUHUZ1.txt")
    elif ((body == "BERAPA SUHU UDARA ZONA DUA SAAT INI\n")  or (body == "TUNJUKKAN SUHU ZONA DUA\n") ):
         shell.Run("balcon -n Vocalizer Damayanti -f SUHUZ2.txt")
    elif ((body == "BERAPA SUHU UDARA ZONA TIGA SAAT INI\n")  or (body == "TUNJUKKAN SUHU ZONA TIGA\n") ):
         shell.Run("balcon -n Vocalizer Damayanti -f SUHUZ3.txt")
    elif ((body == "BERAPA SUHU UDARA ZONA EMPAT SAAT INI\n")  or (body == "TUNJUKKAN SUHU ZONA EMPAT\n") ):
         shell.Run("balcon -n Vocalizer Damayanti -f SUHUZ4.txt")
    elif (body == "NAIKKAN SUHU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NSUHU.txt")
    elif (body == "NAIKKAN SUHU ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NSUHUZ1.txt")
    elif (body == "NAIKKAN SUHU ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NSUHUZ2.txt")
    elif (body == "NAIKKAN SUHU ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NSUHUZ3.txt")
    elif (body == "NAIKKAN SUHU ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NSUHUZ4.txt")
    elif (body == "TURUNKAN SUHU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSUHU.txt")
    elif (body == "TURUNKAN SUHU ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSUHUZ1.txt")
    elif (body == "TURUNKAN SUHU ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSUHUZ2.txt")
    elif (body == "TURUNKAN SUHU ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSUHUZ3.txt")
    elif (body == "TURUNKAN SUHU ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSUHUZ4.txt")
    elif (body == "MATIKAN KIPAS\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f MKIPAS.txt")
    elif (body == "MATIKAN KIPAS ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f MKIPASZ1.txt")
    elif (body == "MATIKAN KIPAS ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f MKIPASZ2.txt")
    elif (body == "MATIKAN KIPAS ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f MKIPASZ3.txt")
    elif (body == "MATIKAN KIPAS ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f MKIPASZ4.txt")
    elif (body == "NYALAKAN KIPAS\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKIPAS.txt")
    elif (body == "NYALAKAN KIPAS ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKIPASZ1.txt")
    elif (body == "NYALAKAN KIPAS ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKIPASZ2.txt")
    elif (body == "NYALAKAN KIPAS ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKIPASZ3.txt")
    elif (body == "NYALAKAN KIPAS ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKIPASZ4.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI SEPULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS10.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI DUA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS20.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI TIGA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS30.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI EMPAT PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS40.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI LIMA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS50.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI ENAM PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS60.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI TUJUH PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS70.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI DELAPAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS80.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI SEMBILAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS90.txt")
    elif (body == "NAIKKAN KECEPATAN KIPAS MENJADI SERATUS PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f NKKIPAS100.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI SEPULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS10.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI DUA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS20.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI TIGA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS30.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI EMPAT PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS40.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI LIMA PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS50.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI ENAM PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS60.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI TUJUH PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS70.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI DELAPAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS80.txt")
    elif (body == "TURUNKAN KECEPATAN KIPAS MENJADI SEMBILAN PULUH PERSEN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TKKIPAS90.txt")
    elif (body == "BERAPA KECEPATAN KIPAS SAAT INI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f BERAPAKK.txt")
    elif (body == "TUNJUKKAN KELEMBAPAN RUANGAN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f KELEMBAPANR.txt")
    elif (body == "TUNJUKKAN KELEMBAPAN RUANGAN ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f KELEMBAPANRZ1.txt")
    elif (body == "TUNJUKKAN KELEMBAPAN RUANGAN ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f KELEMBAPANRZ2.txt")
    elif (body == "TUNJUKKAN KELEMBAPAN RUANGAN ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f KELEMBAPANRZ3.txt")
    elif (body == "TUNJUKKAN KELEMBAPAN RUANGAN ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f KELEMBAPANRZ4.txt")
    elif (body == "TUNJUKKAN TINGKAT KEBISINGAN RUANGAN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TBISING.txt")
    elif (body == "TUNJUKKAN TINGKAT KEBISINGAN RUANGAN ZONA SATU\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TBISINGZ1.txt")
    elif (body == "TUNJUKKAN TINGKAT KEBISINGAN RUANGAN ZONA DUA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TBISINGZ2.txt")
    elif (body == "TUNJUKKAN TINGKAT KEBISINGAN RUANGAN ZONA TIGA\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TBISINGZ3.txt")
    elif (body == "TUNJUKKAN TINGKAT KEBISINGAN RUANGAN ZONA EMPAT\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TBISINGZ4.txt")
    elif (body == "TUNJUKKAN STATUS RUANGAN\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f TSTATUS.txt")
    elif (body == "AKTIFKAN MODE HEMAT ENERGI\n"):
         shell.Run("balcon -n Vocalizer Damayanti -f AKTIFKANMODE.txt")
    #elif (body == "HALO NAMA"):
         #shell.Run("balcon -n Vocalizer Damayanti -t " + contoh)


		 

channel.basic_consume(callback,
                      queue = 'Voice',
					  no_ack = True)


print('Waiting for messages')
channel.start_consuming()
