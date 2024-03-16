import genfont

if __name__ == '__main__':

# gen_sc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
#         prefmy_zh_ui, prefmy_en_ui,
#         cprt_zh, cprt_en, subfmy,
#         weight, weighthuman,
#         out)

# Style = ('Regular', 'Italic', 'Bold', 'Bold Italic')

    print('\n******* start generate 3 sc base fonts *******', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-Regular.ttf', 'SarasaUiSC-Regular.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, '', '',
        'base/msyh.ttc')
    print('*** sc Regular generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-Bold.ttf', 'SarasaUiSC-Bold.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        2, '', '',
        'base/msyhbd.ttc')
    print('*** sc Bold generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-Light.ttf', 'SarasaUiSC-Light.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'Light', 'Light',
        'base/msyhl.ttc')
    print('*** sc Light generated ***', end='\n\n')

    print('\n******* start generate 7 sc supplemental fonts *******', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-Italic.ttf', 'SarasaUiSC-Italic.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, '', '',
        'supplemental/msyhi.ttc')
    print('*** sc Italic generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-BoldItalic.ttf', 'SarasaUiSC-BoldItalic.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        3, '', '',
        'supplemental/msyhbdi.ttc')
    print('*** sc BoldItalic generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-LightItalic.ttf', 'SarasaUiSC-LightItalic.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'Light', 'Light',
        'supplemental/msyhli.ttc')
    print('*** sc LightItalic generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-SemiBold.ttf', 'SarasaUiSC-SemiBold.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'SemiBold', 'SemiBold',
        'supplemental/msyhsb.ttc')
    print('*** sc SemiBold generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-SemiBoldItalic.ttf', 'SarasaUiSC-SemiBoldItalic.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'SemiBold', 'SemiBold',
        'supplemental/msyhsbi.ttc')
    print('*** sc SemiBoldItalic generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-ExtraLight.ttf', 'SarasaUiSC-ExtraLight.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        0, 'ExtraLight', 'XLight',
        'supplemental/msyhxl.ttc')
    print('*** sc ExtraLight generated ***', end='\n\n')

    genfont.gen_sc('SarasaGothicSC-ExtraLightItalic.ttf', 'SarasaUiSC-ExtraLightItalic.ttf',
        '微软雅黑', 'Microsoft YaHei', 'Microsoft YaHei UI', 'Microsoft YaHei UI',
        '更纱to雅黑', 'sarasa2yahei',
        1, 'ExtraLight', 'XLight',
        'supplemental/msyhxli.ttc')
    print('*** sc ExtraLightItalic generated ***', end='\n\n')
