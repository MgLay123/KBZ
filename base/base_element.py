from selenium.webdriver.common.by import By


class BaseElements:
    # 登陆界面
    sidebar_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_open_drawer"
    sidebar_nearby = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/nav_near_by"
    sidebar_feeback = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_help_feedback"
    sidebar_about = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_about"
    lang_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_language"
    lang_en = By.XPATH, "//*[@text = 'English']"
    lang_my = By.XPATH, "//*[@text = 'ျမန္မာ']"
    lang_ch = By.XPATH, "//*[@text = '中文']"
    getcode_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_get_code"
    start_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_start"
    start_button_status = By.XPATH, "//*[@enabled = 'false']"
    phoneNO_input = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_phone_number"
    sms_input = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_verification_code"
    phoneNO = "09770013073"
    smscode = "666888"
    agreement_select = By.XPATH, "//*[@text = 'By starting,I agree to the']"
    title = By.XPATH, "//*[contains(@text, 'ceshi')]"

    # 主页面

    drawer_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_open_drawer"
    notification_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_notification"
    balance_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_home_card"
    scanQR_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_scan_and_pay"
    QR_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_receive_label"
    CashIn_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_cash_in_label"
    CashOut_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_cash_out_label"
    Gift_button = By.XPATH, "//*[@text ='Gift' ]"
    Nearby_button = By.XPATH, "//*[@text ='Nearby' ]"
    Transfer_button = By.XPATH, "//*[@text ='Transfer' ]"
    Topup_button = By.XPATH, "//*[@text ='Top Up' ]"
    Bank_account_button = By.XPATH, "//*[@text ='Bank Account' ]"
    QuickPay_button = By.XPATH, "//*[@text ='Quick Pay' ]"
    History_button = By.XPATH, "//*[@text ='History' ]"

    # 侧边栏

    photo_buttton = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_profile_photo"
    info_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_basic_info"
    limit_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_limit_verification"
    Setting_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_settings"
    Help_feeback_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_help_feedback"
    About_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_about"
    Share_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_share"
    Logout_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_log_out"
    Logout_cancel = By.XPATH, "//*[@text = 'Cancel']"
    Logout_confirm = By.XPATH, "//*[@text = 'Confirm']"

    # 设置照片
    choose_photo_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_choose_album"
    take_photo_button = By.XPATH, "//*[@text = 'Take a Photo']"

    # 设置
    Language_button = By.XPATH, "//*[@text ='Language' ]"
    Notices_button = By.XPATH, "//*[@text ='New Notices' ]"
    Notice_sound_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_sound"
    Notice_vibrate_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_viberate"
    PIN_manage_button = By.XPATH, "//*[@text ='PIN Management' ]"
    Change_pin_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_change_pin"
    Old_pin_input = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_old_pin"
    New_pin_input = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_new_pin"
    Confirm_pin_input = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_confirm_new_pin"
    Confirm_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_confirm"
    Forget_pin_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_reset_pin"
    Reset_now_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_reset_now"
    Edit_KYC = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/editText_no"

    # 帮助与反馈

    Help_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_help"
    Feeback_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_feedback"
    Feeback_more_option = By.XPATH, "//*[@content-desc = 'More options']"
    Feeback_Share = By.XPATH, "//*[@text = 'Share']"
    Feeback_CopyLink = By.XPATH, "//*[@text = 'Copy Link']"
    Feeback_Refresh = By.XPATH, "//*[@text = 'Refresh']"
    Feeback_OpenWith = By.XPATH, "//*[@text = 'Open With']"
    FAQ_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/ll_faq"

    # 提示

    Sys_info_button = By.XPATH, "//*[@text ='System Information' ]"
    Transation_button = By.XPATH, "//*[@text ='Transaction Message' ]"
    News_button = By.XPATH, "//*[@text ='Promotion News' ]"

    # balance

    deposit_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_deposit"
    Cashin_from_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_cash_in_from_agent"
    No_longer_display = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/show_again"
    # Start复用Confirm_button

    Transfer_from_bank_AC = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_transfer_from_bank_account"
    withdraw_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_withdraw"

    # ScanQR

    Album_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_album"
    light_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_flashlight"
    Manual_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/manual"
    Back_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_back"
    Choose_type = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_input_code"
    choose_merchant = By.XPATH, "//*[@text = 'Pay to merchant']"
    choose_agent = By.XPATH, "//*[@text = 'Cash out at agent']"
    choose_person = By.XPATH, "//*[@text = 'Transfer to person']"
    Input_code = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_short_code"
    Enter_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_shortCode_ok"

    # QRcode
    Back_button1 = By.XPATH, "//*[@content-desc = 'Navigate up']"
    Set_Amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_set_amount"
    Save_image = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_save_image"
    Edit_amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_amount"
    Add_note = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_add_note"
    Confirm_button1 = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_ok"

    # cash in
    # 复用back_button1
    Agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_agent"
    # 复用balance
    Bank_account = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_bank_account"

    # Cash Out
    CashOut_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/cash_out_agent"
    At_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/yes_i_am_at_an_agent"
    Edit_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_agent_msisdn"
    Scan_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/scan_agent_msisdn"
    Next_button = By.XPATH, "//*[@text='Next']"
    CashOut_amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/cash_out_amount"
    Cashout_all = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_all"
    MMK800 = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/mmk800"
    Other_amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/et_amount"
    Submit_button = By.XPATH, "//*[@text = 'Submit']"
    Find_agent_map = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/action_nav_to_map"
    Search_agent = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/no_search_for_nearby_agent"

    CashOut_from_ATM = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/tv_cash_out_from_atm"
    CashOut_ATM = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/atm"
    Request_code = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/requst_code_cash_out"
    Search_ATM = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/search_for_nearby_atm"
    PIN_Cancel = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/cancel"
    Forget_pin = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_forget_pin"
    PIN_1 = By.XPATH, "//*[@text = '1']"
    PIN_2 = By.XPATH, "//*[@text = '2']"
    PIN_4 = By.XPATH, "//*[@text = '4']"
    PIN_7 = By.XPATH, "//*[@text = '7']"
    PIN_5 = By.XPATH, "//*[@text = '5']"
    PIN_8 = By.XPATH, "//*[@text = '8']"
    Delete_PIN = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img"

    CashOut_BankAC = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/bank_account"
    CashOut_from_BankAC = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/tv_transfer_from_bank_account"
    # Top UP
    Edit_Phone_no = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_phone_number"
    MMK2000 = By.XPATH, "//*[@text = '2000 MMK']"
    Topup_history = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/top_up_history"
    contact = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_get_contact"
    # Nearby
    Edit_Address = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edit_search"
    Search_button = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/icon_search"

    # Tansfer

    # 复用Edit_Phone_no,Edit_amount,Add_note
    Get_phoneno_contact = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/iv_get_contact"
    Transfer = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_transfer"


    # History
    Filtrate_img = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_filter"
    Min_amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/min_amount"
    Max_amount = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/max_amount"
    Select_salary = By.XPATH, "//*[@text = 'Salary']"
    Reset_filtrate = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/filter_reset"
    Confirm_filtrate = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/filter_sure"

    Date_img = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/img_date_picker"
    From_time = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/from_time_string"
    End_time = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/end_time_string"
    Bt_OK = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_ok"

    # Gift
    Pick_bt = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_template_pick"
    Change_bless_bt = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_change"
    Gift_from_balance = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/btn_from_balance"

    # Quick pay
    Select_Aeon = By.XPATH, "//*[@text = 'Aeon']"
    et_amount = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/et_amount"
    edt_notes = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/edt_notes"
    param_id = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/param_id"
    mother_finance = By.XPATH, "//*[@text = 'Mother Finance Co.,Ltd']"

    # Bank AC
    Add_Bank_AC = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/tv_add_bank_account"
    Edit_Bank_Card_No = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_bank_card_number"
    Edit_code = By.ID, "com.kbzbank.kpaycustomer.ceshi:id/edt_verification_code"
    enter_amount = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/edt_amount"
    romve_bankAC = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/btn_remove_bank_card"
    transfer_to_BankAC = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/btn_balance2ac"
    transfer_from_BankAC = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/btn_ac2balance"
    confirm_no = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/tv_left"
    confirm_yes = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/tv_right"


    #payment

    payment = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/btn_transfer"
    edit_notes = By.ID,"com.kbzbank.kpaycustomer.ceshi:id/edit_note"

    #Display
    ref = "Reference Number"
    assert_pay  = "Payment Successful"
    assert_ATM = "Success"


