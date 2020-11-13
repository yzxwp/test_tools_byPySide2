from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from Method import get_name as name
from Method import get_phone as phone
from Method import get_idcard as idcard
from Method import get_scoure_card as scoure_card
from Method import get_car_vin as vi
from Method import get_zhongzhengma as zzm
from Method import get_bank_card as bank


class Stats():

    def __init__(self):
        try:
            self.ui = QUiLoader().load(r'./UI/message1.ui')
        except:
            self.ui = QUiLoader().load(r'../UI/message1.ui')
        self.ui.pushButton_all.clicked.connect(self.get_all)
        self.ui.pushButton_username.clicked.connect(self.get_name)
        self.ui.pushButton_phone.clicked.connect(self.get_phone)
        self.ui.pushButton_IDCard.clicked.connect(self.get_idcard)
        self.ui.pushButton_shtyzxm.clicked.connect(self.get_shtyzxm)
        self.ui.pushButton_zzjgdm.clicked.connect(self.get_zzjgdm)
        self.ui.pushButton_CJH.clicked.connect(self.get_cjh)
        self.ui.pushButton_zzm.clicked.connect(self.get_zzm)
        self.ui.pushButton_gonghang.clicked.connect(self.get_gonghang)
        self.ui.pushButton_nonghang.clicked.connect(self.get_nonghang)
        self.ui.pushButton_jiaohang.clicked.connect(self.get_jianhang)
        self.ui.pushButton_zhongguo.clicked.connect(self.get_zhongguo)
        self.ui.pushButton_jianshe.clicked.connect(self.get_jianshe)

    def get_all(self):
        self.ui.lineEdit_username.setText(name.random_name())
        print(name.random_name())
        self.ui.lineEdit_phone.setText(phone.phone_num())
        print(phone.phone_num())
        self.ui.lineEdit_IDCard.setText(idcard.ident_generator())
        print(idcard.ident_generator())
        self.ui.lineEdit_shtyzxm.setText(scoure_card.create_social_credit())
        print(scoure_card.create_social_credit())
        self.ui.lineEdit_zzjgdm.setText(scoure_card.create_organization())
        print(scoure_card.create_organization())
        self.ui.lineEdit_CJH.setText(vi.random_vin())
        print(vi.random_vin())
        self.ui.lineEdit_zzm.setText(zzm.ZZM())
        print(zzm.ZZM())
        self.ui.lineEdit_gonghang.setText(bank.gen_bank_card_gonghang())
        print(bank.gen_bank_card_gonghang())
        self.ui.lineEdit_nonghang.setText(bank.gen_bank_card_nonghang())
        print(bank.gen_bank_card_nonghang())
        self.ui.lineEdit_jiaohang.setText(bank.gen_bank_card_jiaotong())
        print(bank.gen_bank_card_jiaotong())
        self.ui.lineEdit_zhongguo.setText(bank.gen_bank_card_zhongguo())
        print(bank.gen_bank_card_zhongguo())
        self.ui.lineEdit_jianshe.setText(bank.gen_bank_card_jainshe())
        print(bank.gen_bank_card_jainshe())

    def get_name(self):
        self.ui.lineEdit_username.setText(name.random_name())
        print(name.random_name())

    def get_phone(self):
        self.ui.lineEdit_phone.setText(phone.phone_num())
        print(phone.phone_num())

    def get_idcard(self):
        self.ui.lineEdit_IDCard.setText(idcard.ident_generator())
        print(idcard.ident_generator())

    def get_shtyzxm(self):
        self.ui.lineEdit_shtyzxm.setText(scoure_card.create_social_credit())
        print(scoure_card.create_social_credit())

    def get_zzjgdm(self):
        self.ui.lineEdit_zzjgdm.setText(scoure_card.create_organization())
        print(scoure_card.create_organization())

    def get_cjh(self):
        self.ui.lineEdit_CJH.setText(vi.random_vin())
        print(vi.random_vin())

    def get_zzm(self):
        self.ui.lineEdit_zzm.setText(zzm.ZZM())
        print(zzm.ZZM())

    def get_gonghang(self):
        self.ui.lineEdit_gonghang.setText(bank.gen_bank_card_gonghang())
        print(bank.gen_bank_card_gonghang())

    def get_nonghang(self):
        self.ui.lineEdit_nonghang.setText(bank.gen_bank_card_nonghang())
        print(bank.gen_bank_card_nonghang())

    def get_jianhang(self):
        self.ui.lineEdit_jiaohang.setText(bank.gen_bank_card_jiaotong())
        print(bank.gen_bank_card_jiaotong())

    def get_zhongguo(self):
        self.ui.lineEdit_zhongguo.setText(bank.gen_bank_card_zhongguo())
        print(bank.gen_bank_card_zhongguo())

    def get_jianshe(self):
        self.ui.lineEdit_jianshe.setText(bank.gen_bank_card_jainshe())
        print(bank.gen_bank_card_jainshe())


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
