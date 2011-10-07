"""Auto-generated file, do not edit by hand. AR metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_AR = PhoneMetadata(id='AR', country_code=54, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-8]\\d{9}|9\\d{10}', possible_number_pattern='\\d{6,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='11\\d{8}|(?:2(?:2(?:[0139]\\d|2[13-79]|4[1-6]|5[2457]|6[124-8]|7[1-4]|8[13-6])|3(?:1[467]|2[02-6]|3[13-8]|[49][2-6]|5[2-8]|[067]\\d)|47[3-8]|6(?:[01345]\\d|2[2-7])|9(?:[0124789]\\d|3[1-6]|5[234]|6[2-6]))|3(?:3(?:2[79]|8[2578])|4(?:[78]\\d|0[0124-9]|[1-356]\\d|4[24-7]|9[123678])|5(?:[138]\\d|2[1245]|4[1-9]|6[2-4]|7[1-6])|7(?:[12468]\\d|3[1245]|5[124-8]|7[2-57])|8(?:[123578]\\d|4[13-6]6[1-357-9]|9[124]))|670\\d)\\d{6}', possible_number_pattern='\\d{6,10}', example_number='1123456789'),
    mobile=PhoneNumberDesc(national_number_pattern='675\\d{7}|9(?:11[2-9]\\d{7}|(?:2(?:2[013]|37|6[14]|9[179])|3(?:4[1235]|5[138]|8[1578]))[2-9]\\d{6}|\\d{4}[2-9]\\d{5})', possible_number_pattern='\\d{6,11}', example_number='91123456789'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{7}', possible_number_pattern='\\d{10}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='60[04579]\\d{7}', possible_number_pattern='\\d{10}', example_number='6001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='810\\d{7}', possible_number_pattern='\\d{10}', example_number='8101234567'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='810\\d{7}', possible_number_pattern='\\d{10}', example_number='8101234567'),
    national_prefix=u'0',
    national_prefix_for_parsing=u'0(?:(11|2(?:2(?:02?|[13]|2[13-79]|4[1-6]|5[2457]|6[124-8]|7[1-4]|8[13-6]|9[1-367])|3(?:[06]2|1[467]|2[02-6]|3[13-8]|[49][2-6]|5[2-8]|7)|47[3-578]|6(?:1|2[2-7]|4[6-8]?|5[125-8])|9(?:0[1-3]|[19]|2\d|3[1-6]|4[0-24-68]|5[2-4]|6[2-6]|72?|8[23]?))|3(?:3(?:2[79]|8[2578])|4(?:0[124-9]|[12]|3[5-8]?|4[24-7]|5[4-68]?|6\d|7[126]|8[237-9]|9[1-36-8])|5(?:1|2[1245]|3[2-4]?|4[1-46-9]|6[2-4]|7[1-6]|8[2-5]?)|7(?:1[15-8]|2[125]|3[1245]|4[13]|5[124-8]|7[2-57]|8[1-36])|8(?:1|2[125-7]|3[23578]|4[13-6]|5[4-8]?|6[1-357-9]|7[5-8]?|8[4-7]?|9[124])))15)?',
    national_prefix_transform_rule=u'9\\1',
    number_format=[NumberFormat(pattern='([68]\\d{2})(\\d{3})(\\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[68]'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9)(11)(\\d{4})(\\d{4})', format=u'\\2 15-\\3-\\4', leading_digits_pattern=['911'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9)(\\d{3})(\\d{3})(\\d{4})', format=u'\\2 15-\\3-\\4', leading_digits_pattern=['9(?:2[2369]|3[458])', '9(?:2(?:2[013]|37|6[14]|9[179])|3(?:4[1235]|5[138]|8[1578]))'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(9)(\\d{4})(\\d{2})(\\d{4})', format=u'\\2 15-\\3-\\4', leading_digits_pattern=['9(?:2[2-469]|3[3-578])', '9(?:2(?:2[24-9]|3[0-69]|47|6[25]|9[02-68])|3(?:3[28]|4[046-9]|5[2467]|7[1-578]|8[23469]))'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(11)(\\d{4})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['1'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['2(?:2[013]|37|6[14]|9[179])|3(?:4[1235]|5[138]|8[1578])'], national_prefix_formatting_rule=u'0\\1'),
        NumberFormat(pattern='(\\d{4})(\\d{2})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['[23]'], national_prefix_formatting_rule=u'0\\1')],
    intl_number_format=[NumberFormat(pattern='([68]\\d{2})(\\d{3})(\\d{4})', format=u'\\1-\\2-\\3', leading_digits_pattern=['[68]']),
        NumberFormat(pattern='(9)(11)(\\d{4})(\\d{4})', format=u'\\1 \\2 \\3-\\4', leading_digits_pattern=['911']),
        NumberFormat(pattern='(9)(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2 \\3-\\4', leading_digits_pattern=['9(?:2[2369]|3[458])', '9(?:2(?:2[013]|37|6[14]|9[179])|3(?:4[1235]|5[138]|8[1578]))']),
        NumberFormat(pattern='(9)(\\d{4})(\\d{2})(\\d{4})', format=u'\\1 \\2 \\3-\\4', leading_digits_pattern=['9(?:2[2-469]|3[3-578])', '9(?:2(?:2[24-9]|3[0-69]|47|6[25]|9[02-68])|3(?:3[28]|4[046-9]|5[2467]|7[1-578]|8[23469]))']),
        NumberFormat(pattern='(11)(\\d{4})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['1']),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['2(?:2[013]|37|6[14]|9[179])|3(?:4[1235]|5[138]|8[1578])']),
        NumberFormat(pattern='(\\d{4})(\\d{2})(\\d{4})', format=u'\\1 \\2-\\3', leading_digits_pattern=['[23]'])])
