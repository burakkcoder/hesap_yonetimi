from tkinter import *
from tkinter import messagebox
import os


def giris():
    klnc = kullanici_adi.get()
    prl = parola.get()

    if klnc == "Burakcode" and prl == "123654":
        root = Toplevel()
        root.title("Hesap Yönetimi")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False, False)
        icon_img = PhotoImage(file="hesapp.png")
        root.iconphoto(False, icon_img)

        Label(root, text="HESAP YÖNETİMİ", bg="black", fg="white",
              font=("calibri", 33), width="300", height="4").pack()

        # MENÜ
        menu = Frame(root, bg="lightgreen", highlightbackground="black",
                     highlightthickness=1, width=370, height=400)
        menu.place(x=30, y=250)

        Label(menu, text="Menü", font=("Gabriola", 40, "bold"),
              fg="black", bg="lightgreen").place(x=100, y=0)

        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Sandviç ....................... 60 ₺", fg="black", bg="lightgreen").place(x=10, y=80)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Kurabiye .................... 30 ₺", fg="black", bg="lightgreen").place(x=10, y=110)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Çay .............................. 7 ₺", fg="black", bg="lightgreen").place(x=10, y=140)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Kahve ......................... 100 ₺", fg="black", bg="lightgreen").place(x=10, y=170)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Meyve Suyu ............... 20 ₺", fg="black", bg="lightgreen").place(x=10, y=200)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Kek ............................. 15 ₺", fg="black", bg="lightgreen").place(x=10, y=230)
        Label(menu, font=("Lucida Calligraphy", 15, "bold"),
              text="Börek .......................... 25 ₺", fg="black", bg="lightgreen").place(x=10, y=260)

        # HESAP
        hesap_bolumu = Frame(root, bg="lightyellow", highlightbackground="black",
                             highlightthickness=1, width=370, height=400)
        hesap_bolumu.place(x=880, y=250)

        hesap = Label(hesap_bolumu, text="Hesap", font=(
            "calibri", 20), bg="lightyellow")
        hesap.place(x=160, y=10)

        # ÜRÜN GİRİŞLERi
        urunler = Frame(root, bd=5, height=400, width=450, relief=RAISED)
        urunler.pack(pady=30)

        sandvic = StringVar()
        kurabiye = StringVar()
        cay = StringVar()
        kahve = StringVar()
        meyve_suyu = StringVar()
        kek = StringVar()
        borek = StringVar()
        toplam = StringVar()

        lbl_sandvic = Label(urunler, font=("arial", 20, "bold"),
                            text="Sandviç", width=12, fg="blue4")
        lbl_kurabiye = Label(urunler, font=(
            "arial", 20, "bold"), text="Kurabiye", width=12, fg="blue4")
        lbl_cay = Label(urunler, font=("arial", 20, "bold"),
                        text="Çay", width=12, fg="blue4")
        lbl_kahve = Label(urunler, font=("arial", 20, "bold"),
                          text="Kahve", width=12, fg="blue4")
        lbl_meyve_suyu = Label(urunler, font=(
            "arial", 20, "bold"), text="Meyve Suyu", width=12, fg="blue4")
        lbl_kek = Label(urunler, font=("arial", 20, "bold"),
                        text="Kek", width=12, fg="blue4")
        lbl_borek = Label(urunler, font=("arial", 20, "bold"),
                          text="Börek", width=12, fg="blue4")

        lbl_sandvic.grid(row=1, column=0)
        lbl_kurabiye.grid(row=2, column=0)
        lbl_cay.grid(row=3, column=0)
        lbl_kahve.grid(row=4, column=0)
        lbl_meyve_suyu.grid(row=5, column=0)
        lbl_kek.grid(row=6, column=0)
        lbl_borek.grid(row=7, column=0)

        sandvic_giris = Entry(urunler, font=(
            "arial", 20, "bold"), textvariable=sandvic, bd=6, width=8, bg="lightpink")
        kurabiye_giris = Entry(urunler, font=(
            "arial", 20, "bold"), textvariable=kurabiye, bd=6, width=8, bg="lightpink")
        cay_giris = Entry(urunler, font=("arial", 20, "bold"),
                          textvariable=cay, bd=6, width=8, bg="lightpink")
        kahve_giris = Entry(urunler, font=("arial", 20, "bold"),
                            textvariable=kahve, bd=6, width=8, bg="lightpink")
        meyve_suyu_giris = Entry(urunler, font=(
            "arial", 20, "bold"), textvariable=meyve_suyu, bd=6, width=8, bg="lightpink")
        kek_giris = Entry(urunler, font=("arial", 20, "bold"),
                          textvariable=kek, bd=6, width=8, bg="lightpink")
        borek_giris = Entry(urunler, font=("arial", 20, "bold"),
                            textvariable=borek, bd=6, width=8, bg="lightpink")

        sandvic_giris.grid(row=1, column=1)
        kurabiye_giris.grid(row=2, column=1)
        cay_giris.grid(row=3, column=1)
        kahve_giris.grid(row=4, column=1)
        meyve_suyu_giris.grid(row=5, column=1)
        kek_giris.grid(row=6, column=1)
        borek_giris.grid(row=7, column=1)

        def urunleriSifirla():
            sandvic_giris.delete(0, END)
            kurabiye_giris.delete(0, END)
            cay_giris.delete(0, END)
            kahve_giris.delete(0, END)
            meyve_suyu_giris.delete(0, END)
            kek_giris.delete(0, END)
            borek_giris.delete(0, END)

        def urunlerToplami():
            try:
                urun1 = int(sandvic.get())
            except:
                urun1 = 0
            try:
                urun2 = int(kurabiye.get())
            except:
                urun2 = 0
            try:
                urun3 = int(cay.get())
            except:
                urun3 = 0
            try:
                urun4 = int(kahve.get())
            except:
                urun4 = 0
            try:
                urun5 = int(meyve_suyu.get())
            except:
                urun5 = 0
            try:
                urun6 = int(kek.get())
            except:
                urun6 = 0
            try:
                urun7 = int(borek.get())
            except:
                urun7 = 0

            lbl_toplam = Label(hesap_bolumu, font=(
                "arial", 20, "bold"), text="Toplam", width=22, fg="lightyellow", bg="black")
            lbl_toplam.place(x=0, y=50)
            toplam_giris = Entry(hesap_bolumu, font=(
                "arial", 20, "bold"), textvariable=toplam, bd=6, width=14, bg="lightgreen")
            toplam_giris.place(x=80, y=100)

            urunlerinToplami = (urun1 * 60) + (urun2 * 30) + (urun3 * 7) + \
                (urun4 * 100) + (urun5 * 20) + (urun6 * 15) + (urun7 * 7)
            str_urun_toplami = str("%.2f" % urunlerinToplami)
            toplam.set(str_urun_toplami)

        # BUTONLAR
        sifirla_butonu = Button(urunler, bd=5, fg="black", bg="lightblue", font=(
            "arial", 16, "bold"), width=10, text="Sıfırla", command=urunleriSifirla)
        sifirla_butonu.grid(row=8, column=0)
        toplam_butonu = Button(urunler, bd=5, fg="black", bg="lightblue", font=(
            "arial", 16, "bold"), width=10, text="Toplam", command=urunlerToplami)
        toplam_butonu.grid(row=8, column=1)

    elif klnc == "" and prl == "":
        messagebox.showerror("Hata", "Lütfen kullanıcı adı ve parolayı girin.")
    elif klnc == "":
        messagebox.showerror("Hata", "Lütfen kullanıcı adını girin.")
    elif prl == "":
        messagebox.showerror("Hata", "Lütfen parolayı girin.")
    elif klnc != "Burakcode" and prl != "123654":
        messagebox.showerror("Hata", "Kullanıcı adı ve parola hatalı!")
    elif klnc != "Burakcode":
        messagebox.showerror("Hata", "Kullanıcı adı hatalı!")
    elif prl != "123654":
        messagebox.showerror("Hata", "Parola hatalı!")


def anaEkran():
    global ekran
    global kullanici_adi
    global parola

    ekran = Tk()
    ekran.geometry("1280x720+150+80")
    ekran.configure(bg="#d7dae2")

    # Icon
    icon_img = PhotoImage(file="loginn.png")
    ekran.iconphoto(False, icon_img)
    ekran.title("Giriş Ekranı")

    baslik_lbl = Label(text="Giriş Ekranı", font=(
        "arial", 50, "bold"), fg="black", bg="#d7dae2")
    baslik_lbl.pack(pady=50)

    # Giriş Bölümü Çerçeve
    bordercolor = Frame(ekran, bg="black", width=800, height=400)
    bordercolor.pack()
    anaFrame = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    anaFrame.pack(padx=20, pady=20)

    # Kullanıcı Giriş Bölümü
    kullanici_adi = StringVar()
    parola = StringVar()

    kullanici_adi_giris = Entry(
        anaFrame, textvariable=kullanici_adi, width=12, bd=2, font=("arial", 30))
    kullanici_adi_giris.place(x=400, y=50)
    parola_giris = Entry(anaFrame, textvariable=parola,
                         width=12, bd=2, font=("arial", 30), show="*")
    parola_giris.place(x=400, y=150)

    Label(anaFrame, text="Kullanıcı Adı", font=(
        "arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(anaFrame, text="Parola", font=("arial", 30, "bold"),
          bg="#d7dae2").place(x=100, y=150)

    def sifirla():
        kullanici_adi_giris.delete(0, END)
        parola_giris.delete(0, END)

    Button(anaFrame, text="Giriş", height="2", width=23, bg="#00bd56",
           fg="white", bd=0, command=giris).place(x=100, y=250)
    Button(anaFrame, text="Sıfırla", height="2", width=23, bg="#1089ff",
           fg="white", bd=0, command=sifirla).place(x=300, y=250)
    Button(anaFrame, text="Çıkış", height="2", width=23, bg="#ed3833",
           fg="white", bd=0, command=ekran.destroy).place(x=500, y=250)

    ekran.mainloop()


anaEkran()
