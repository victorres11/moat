from flask import Flask, request, jsonify, render_template, make_response
import os

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template("moat_template.html")

@app.route('/process_inputs')
def process_inputs():
    agency_input = request.args.get('agency_input').lower()
    platform_input = request.args.get('platform_input').lower()

    TTD_tag = '<noscript class="MOAT-taykeytradedeskdisplay372494051270?moatClientLevel1={}&amp;moatClientLevel2=%%TTD_CAMPAIGNID%%&amp;moatClientLevel3=%%TTD_ADGROUPID%%&amp;moatClientLevel4=%%TTD_CREATIVEID%%&amp;moatClientSlicer1=%%TTD_SUPPLYVENDOR%%&amp;moatClientSlicer2=%%TTD_SITE%%"></noscript><script src="https://z.moatads.com/taykeytradedeskdisplay372494051270/moatad.js#moatClientLevel1=%s&moatClientLevel2=%%TTD_CAMPAIGNID%%&moatClientLevel3=%%TTD_ADGROUPID%%&moatClientLevel4=%%TTD_CREATIVEID%%&moatClientSlicer1=%%TTD_SUPPLYVENDOR%%&moatClientSlicer2=%%TTD_SITE%%" type="text/javascript"></script>'.format(agency_input, agency_input)
    APN_tag = 'https://z.moatads.com/taykeyappnexus641609674048/moatad.js#moatClientLevel1=%s&moatClientLevel2=${CPG_ID}&moatClientLevel3=${CP_ID}&moatClientLevel4=${CREATIVE_ID}&moatClientSlicer1=${REFERER_URL_ENC}' % (agency_input)

    if platform_input == 'y':
        response = make_response(TTD_tag)
        response.headers["Content-Disposition"] = "attachment; filename=TTD_DISPLAY_MOAT_%s.txt" % (agency_input)
    else if platorm_input == 'n':
        response = make_response(APN_tag)
        response.headers["Content-Disposition"] = "attachment; filename=APN_DISPLAY_MOAT_%s.txt" % (agency_input)

    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
