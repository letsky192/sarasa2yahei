import fontforge as ff

DOWNLOAD_DIR = '/tmp/fonts'
OUTPUT_DIR_SC = '/tmp/fonts/sc'
OUTPUT_DIR_TC = '/tmp/fonts/tc'


def open_font(path):
    return ff.open(path)

def close_font(font):
    font.close()

# def get_version(font):
#     return font.version.split(';')[0]


Style = ('Regular', 'Italic', 'Bold', 'Bold Italic')

def set_font_info_sc(font, prefmy_zh, prefmy_en,
                    cprt_zh, cprt_en, subfmy,
                    weight='', weighthuman=''):

    if len(weight)>0:
        preferredstyles = (f'{weight} {Style[subfmy]}' if subfmy>0 else weight)
        familyname_en = f'{prefmy_en} {weighthuman}'
        familyname_zh = f'{prefmy_zh} {weighthuman}'
        fullname_en = (f'{familyname_en} {Style[subfmy]}'
                        if subfmy>0 else familyname_en)
        fullname_zh = (f'{familyname_zh} {Style[subfmy]}'
                        if subfmy>0 else familyname_zh)
        uniqueid_en = f'{prefmy_en} {preferredstyles}'
        uniqueid_zh = f'{prefmy_zh} {preferredstyles}'
    else:
        preferredstyles = Style[subfmy]
        familyname_en = prefmy_en
        familyname_zh = prefmy_zh
        fullname_en = (f'{familyname_en} {Style[subfmy]}'
                        if subfmy>0 else familyname_en)
        fullname_zh = (f'{familyname_zh} {Style[subfmy]}'
                        if subfmy>0 else familyname_zh)
        uniqueid_en = f'{prefmy_en} {preferredstyles}'
        uniqueid_zh = f'{prefmy_zh} {preferredstyles}'

    font.fontname = prefmy_en.replace(' ','')+'-'+preferredstyles.replace(' ','')
    font.familyname = familyname_en
    font.fullname = fullname_en
#    font.version = get_version(font)
    font.copyright = cprt_en
    font.sfnt_names = (
        ('English (US)', 'Copyright', cprt_en),
        ('English (US)', 'Family', familyname_en),
        ('English (US)', 'SubFamily', Style[subfmy]),
        ('English (US)', 'UniqueID', uniqueid_en),
        ('English (US)', 'Fullname', fullname_en),
        ('English (US)', 'Version', font.version),
        ('English (US)', 'PostScriptName', font.fontname),
        ('English (US)', 'Preferred Family', prefmy_en),
        ('English (US)', 'Preferred Styles', preferredstyles),
        ('Chinese (PRC)', 'Copyright', cprt_zh),
        ('Chinese (PRC)', 'Family', familyname_zh),
        ('Chinese (PRC)', 'SubFamily', Style[subfmy]),
        ('Chinese (PRC)', 'UniqueID', uniqueid_zh),
        ('Chinese (PRC)', 'Fullname', fullname_zh),
        ('Chinese (PRC)', 'Version', font.version),
        ('Chinese (PRC)', 'Preferred Family', prefmy_zh),
        ('Chinese (PRC)', 'Preferred Styles', preferredstyles)
    )


def set_font_info_tc(font, prefmy_zh, prefmy_en,
                    cprt_zh, cprt_en, subfmy,
                    weight='', weighthuman=''):

    if len(weight)>0:
        preferredstyles = (f'{weight} {Style[subfmy]}' if subfmy>0 else weight)
        familyname_en = f'{prefmy_en} {weighthuman}'
        familyname_zh = f'{prefmy_zh} {weighthuman}'
        fullname_en = (f'{familyname_en} {Style[subfmy]}'
                        if subfmy>0 else familyname_en)
        fullname_zh = (f'{familyname_zh} {Style[subfmy]}'
                        if subfmy>0 else familyname_zh)
        uniqueid_en = f'{prefmy_en} {preferredstyles}'
        uniqueid_zh = f'{prefmy_zh} {preferredstyles}'
    else:
        preferredstyles = Style[subfmy]
        familyname_en = prefmy_en
        familyname_zh = prefmy_zh
        fullname_en = (f'{familyname_en} {Style[subfmy]}'
                        if subfmy>0 else familyname_en)
        fullname_zh = (f'{familyname_zh} {Style[subfmy]}'
                        if subfmy>0 else familyname_zh)
        uniqueid_en = f'{prefmy_en} {preferredstyles}'
        uniqueid_zh = f'{prefmy_zh} {preferredstyles}'

    font.fontname = prefmy_en.replace(' ','')+'-'+preferredstyles.replace(' ','')
    font.familyname = familyname_en
    font.fullname = fullname_en
#    font.version = get_version(font)
    font.copyright = cprt_en
    font.sfnt_names = (
        ('English (US)', 'Copyright', cprt_en),
        ('English (US)', 'Family', familyname_en),
        ('English (US)', 'SubFamily', Style[subfmy]),
        ('English (US)', 'UniqueID', uniqueid_en),
        ('English (US)', 'Fullname', fullname_en),
        ('English (US)', 'Version', font.version),
        ('English (US)', 'PostScriptName', font.fontname),
        ('English (US)', 'Preferred Family', prefmy_en),
        ('English (US)', 'Preferred Styles', preferredstyles),
        ('Chinese (Taiwan)', 'Copyright', cprt_zh),
        ('Chinese (Taiwan)', 'Family', familyname_zh),
        ('Chinese (Taiwan)', 'SubFamily', Style[subfmy]),
        ('Chinese (Taiwan)', 'UniqueID', uniqueid_zh),
        ('Chinese (Taiwan)', 'Fullname', fullname_zh),
        ('Chinese (Taiwan)', 'Version', font.version),
        ('Chinese (Taiwan)', 'Preferred Family', prefmy_zh),
        ('Chinese (Taiwan)', 'Preferred Styles', preferredstyles),
        ('Chinese (Hong Kong)', 'Copyright', cprt_zh),
        ('Chinese (Hong Kong)', 'Family', familyname_zh),
        ('Chinese (Hong Kong)', 'SubFamily', Style[subfmy]),
        ('Chinese (Hong Kong)', 'UniqueID', uniqueid_zh),
        ('Chinese (Hong Kong)', 'Fullname', fullname_zh),
        ('Chinese (Hong Kong)', 'Version', font.version),
        ('Chinese (Hong Kong)', 'Preferred Family', prefmy_zh),
        ('Chinese (Hong Kong)', 'Preferred Styles', preferredstyles)
    )


def bytes2int(bytes):
    return int.from_bytes(bytes, byteorder='big', signed=False)


def readXACW(ttffile):
    fo = open(ttffile, 'rb')
    HeadBytes = fo.read(224)
    index = HeadBytes.find(b'OS/2') + 8
    offset = bytes2int(HeadBytes[index:index+4])
    fo.seek(offset + 2, 0)
    XACW_Bytes = fo.read(2)
    fo.close()
    print(f'read {ttffile}')
    XACW = bytes2int(XACW_Bytes)
    print(f'xAvgCharWidth = {XACW}')
    return XACW_Bytes


def patchXACW(ttcfile, XACW_Bytes1, XACW_Bytes2):
    fo = open(ttcfile, 'rb+')
    assert (fo.read(4) == b'ttcf'), '不是 ttc 文件'
    fo.seek(8, 0)
    assert (fo.read(4) == b'\x00\x00\x00\x02'), 'ttc 中字体数量不是 2'

    OffsetTtfHead_Bytes1 = fo.read(4)
    OffsetTtfHead_Bytes2 = fo.read(4)
    fo.seek(bytes2int(OffsetTtfHead_Bytes1), 0)
    HeadBytes1 = fo.read(224)
    fo.seek(bytes2int(OffsetTtfHead_Bytes2), 0)
    HeadBytes2 = fo.read(224)
    index1 = HeadBytes1.find(b'OS/2') + 8
    index2 = HeadBytes2.find(b'OS/2') + 8
    offset1 = bytes2int(HeadBytes1[index1:index1+4])
    offset2 = bytes2int(HeadBytes2[index2:index2+4])

    fo.seek(offset1 + 2, 0)
    oldXACW_Bytes1 = fo.read(2)
    fo.seek(offset2 + 2, 0)
    oldXACW_Bytes2 = fo.read(2)

    fo.seek(offset1 + 2, 0)
    fo.write(XACW_Bytes1)
    fo.seek(offset2 + 2, 0)
    fo.write(XACW_Bytes2)
    fo.close()

    print(f'patch {ttcfile}')
    oldXACW1 = bytes2int(oldXACW_Bytes1)
    oldXACW2 = bytes2int(oldXACW_Bytes2)
    XACW1 = bytes2int(XACW_Bytes1)
    XACW2 = bytes2int(XACW_Bytes2)
    print('xAvgCharWidth Fixing:')
    print(f'{oldXACW1} --> {XACW1}')
    print(f'{oldXACW2} --> {XACW2}')
    return
