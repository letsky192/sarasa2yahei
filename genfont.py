import utils


def gen_sc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
            prefmy_zh_ui, prefmy_en_ui,
            cprt_zh, cprt_en, subfmy,
            weight, weighthuman,
            out):

    font = utils.open_font(utils.DOWNLOAD_DIR + '/' + sarasa)
    utils.set_font_info_sc(font, prefmy_zh, prefmy_en,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/' + sarasa_ui)
    utils.set_font_info_sc(font_ui, prefmy_zh_ui, prefmy_en_ui,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font.generateTtc(utils.OUTPUT_DIR_SC+'/'+out, font_ui, ttcflags = ('merge'), layer = 1)
    utils.close_font(font)
    utils.close_font(font_ui)

# set_font_info_sc(font, prefmy_zh, prefmy_en,
#                 cprt_zh, cprt_en, subfmy,
#                 weight='', weighthuman='')

# Style = ('Regular', 'Italic', 'Bold', 'Bold Italic')


def gen_tc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
            prefmy_zh_ui, prefmy_en_ui,
            cprt_zh, cprt_en, subfmy,
            weight, weighthuman,
            out):

    font = utils.open_font(utils.DOWNLOAD_DIR + '/' + sarasa)
    utils.set_font_info_tc(font, prefmy_zh, prefmy_en,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/' + sarasa_ui)
    utils.set_font_info_tc(font_ui, prefmy_zh_ui, prefmy_en_ui,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font.generateTtc(utils.OUTPUT_DIR_TC+'/'+out, font_ui, ttcflags = ('merge'), layer = 1)
    utils.close_font(font)
    utils.close_font(font_ui)
