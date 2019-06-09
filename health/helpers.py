def generate_hosp_list(hosps):
    result_html = ''
    for good_hosp in hosps:
        result_html += f"""
                <div class="item">
                    <div class="item-img-div">
                        <img class="item-img" src="static/health/cat.jpg">
                    </div>
                    <div class="item-text">
                        <div class="item-name">{good_hosp['name']}</div>
                        <p>Where: {good_hosp['addr']}</p>
                        <p>Здесь будет информация...</p>
                    </div>
                </div>"""

    return result_html
