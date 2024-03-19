import utils


def gen_sc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
            prefmy_zh_ui, prefmy_en_ui,
            cprt_zh, cprt_en, subfmy,
            weight, weighthuman,
            out):

    file1 = utils.DOWNLOAD_DIR + '/' + sarasa
    file2 = utils.DOWNLOAD_DIR + '/' + sarasa_ui
    outfile = utils.OUTPUT_DIR_SC + '/' + out

    font = utils.open_font(file1)
    utils.set_font_info_sc(font, prefmy_zh, prefmy_en,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font_ui = utils.open_font(file2)
    utils.set_font_info_sc(font_ui, prefmy_zh_ui, prefmy_en_ui,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font.generateTtc(outfile, font_ui, ttcflags = ('merge'), layer = font.activeLayer)
    utils.close_font(font)
    utils.close_font(font_ui)
    XACW_Bytes1 = utils.readXACW(file1)
    XACW_Bytes2 = utils.readXACW(file2)
    utils.patchXACW(outfile, XACW_Bytes1, XACW_Bytes2)

# set_font_info_sc(font, prefmy_zh, prefmy_en,
#                 cprt_zh, cprt_en, subfmy,
#                 weight='', weighthuman='')

# Style = ('Regular', 'Italic', 'Bold', 'Bold Italic')

def gen_tc(sarasa, sarasa_ui, prefmy_zh, prefmy_en,
            prefmy_zh_ui, prefmy_en_ui,
            cprt_zh, cprt_en, subfmy,
            weight, weighthuman,
            out):

    file1 = utils.DOWNLOAD_DIR + '/' + sarasa
    file2 = utils.DOWNLOAD_DIR + '/' + sarasa_ui
    outfile = utils.OUTPUT_DIR_TC + '/' + out

    font = utils.open_font(file1)
    utils.set_font_info_tc(font, prefmy_zh, prefmy_en,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font_ui = utils.open_font(file2)
    utils.set_font_info_tc(font_ui, prefmy_zh_ui, prefmy_en_ui,
                        cprt_zh, cprt_en, subfmy,
                        weight, weighthuman)

    font.generateTtc(outfile, font_ui, ttcflags = ('merge'), layer = font.activeLayer)
    utils.close_font(font)
    utils.close_font(font_ui)
    XACW_Bytes1 = utils.readXACW(file1)
    XACW_Bytes2 = utils.readXACW(file2)
    utils.patchXACW(outfile, XACW_Bytes1, XACW_Bytes2)
