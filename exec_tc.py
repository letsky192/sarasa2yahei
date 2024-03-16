import genfont

if __name__ == '__main__':

# gen_tc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
#         prefmy_zh_ui, prefmy_en_ui,
#         cprt_zh, cprt_en, subfmy,
#         weight, weighthuman,
#         out)

# Style = ('Regular', 'Italic', 'Bold', 'Bold Italic')

    print('\n******* start generate 3 tc base fonts *******', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-Regular.ttf', 'SarasaUiTC-Regular.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, '', '',
        'base/msjh.ttc')
    print('*** tc Regular generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-Bold.ttf', 'SarasaUiTC-Bold.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        2, '', '',
        'base/msjhbd.ttc')
    print('*** tc Bold generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-Light.ttf', 'SarasaUiTC-Light.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'Light', 'Light',
        'base/msjhl.ttc')
    print('*** tc Light generated ***', end='\n\n')

    print('\n******* start generate 7 tc supplemental fonts *******', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-Italic.ttf', 'SarasaUiTC-Italic.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, '', '',
        'supplemental/msjhi.ttc')
    print('*** tc Italic generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-BoldItalic.ttf', 'SarasaUiTC-BoldItalic.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        3, '', '',
        'supplemental/msjhbdi.ttc')
    print('*** tc BoldItalic generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-LightItalic.ttf', 'SarasaUiTC-LightItalic.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'Light', 'Light',
        'supplemental/msjhli.ttc')
    print('*** tc LightItalic generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-SemiBold.ttf', 'SarasaUiTC-SemiBold.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'SemiBold', 'SemiBold',
        'supplemental/msjhsb.ttc')
    print('*** tc SemiBold generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-SemiBoldItalic.ttf', 'SarasaUiTC-SemiBoldItalic.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'SemiBold', 'SemiBold',
        'supplemental/msjhsbi.ttc')
    print('*** tc SemiBoldItalic generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-ExtraLight.ttf', 'SarasaUiTC-ExtraLight.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'ExtraLight', 'XLight',
        'supplemental/msjhxl.ttc')
    print('*** tc ExtraLight generated ***', end='\n\n')

    genfont.gen_tc('SarasaGothicTC-ExtraLightItalic.ttf', 'SarasaUiTC-ExtraLightItalic.ttf',
        '微軟正黑體', 'Microsoft JhengHei', 'Microsoft JhengHei UI', 'Microsoft JhengHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'ExtraLight', 'XLight',
        'supplemental/msjhxli.ttc')
    print('*** tc ExtraLightItalic generated ***', end='\n\n')
