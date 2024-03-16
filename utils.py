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
