from app import app

VALID_FORM = {
    "height": "170",
    "weight": "65",
    "HighBP": "0",
    "HighChol": "0",
    "GenHlth": "1",
    "Age": "1",
}


def get_client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page_loads():
    response = get_client().get("/")
    assert response.status_code == 200


def test_about_and_profile_pages_load():
    client = get_client()
    assert client.get("/about").status_code == 200
    assert client.get("/profile").status_code == 200


def test_predict_valid_input_shows_a_result():
    response = get_client().post("/predict", data=VALID_FORM)
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Tidak Diabetes" in html or "Positif Diabetes" in html


def test_predict_non_numeric_height_shows_error():
    form = dict(VALID_FORM)
    form["height"] = "abc"
    response = get_client().post("/predict", data=form)
    assert response.status_code == 200
    assert "Input tidak valid" in response.get_data(as_text=True)


def test_predict_missing_field_shows_error():
    form = dict(VALID_FORM)
    del form["weight"]
    response = get_client().post("/predict", data=form)
    assert "Input tidak valid" in response.get_data(as_text=True)


def test_predict_zero_height_is_rejected():
    form = dict(VALID_FORM)
    form["height"] = "0"
    response = get_client().post("/predict", data=form)
    assert response.status_code == 200
    assert "Input tidak valid" in response.get_data(as_text=True)