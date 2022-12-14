fn main() {
    let response = reqwest::blocking::get("https://crypto.com/price")
        .unwrap()
        .text()
        .unwrap();

    let document = scraper::Html::parse_document(&response);
    let crypto_selector = scraper::Selector::parse(".css-1cxc880").unwrap();

    let crypto_name_selector = scraper::Selector::parse(".css-rkws3").unwrap();
    let crypto_price_selector = scraper::Selector::parse("td div.css-0").unwrap();
    let crypto_24_change_selector = scraper::Selector::parse("td.css-1b7j986").unwrap();
    let crypto_24_vol_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();
    let crypto_marketcap_selector = scraper::Selector::parse("td.css-1nh9lk8+td.css-1nh9lk8").unwrap();

    let mut wtr = csv::Writer::from_path("cryptoData.csv").expect("Could not create file.");
    wtr.write_record(&["Crypto", "Price", "24HrChange", "24HrVol", "Marketcap"]).expect("Could not write header.");

    for element in document.select(&crypto_selector) {

        let crypto_name_element = element
            .select(&crypto_name_selector)
            .next()
            .expect("Could not load the crypto");
        let crypto_name = crypto_name_element.text().collect::<String>();

        let crypto_price_element = element
            .select(&crypto_price_selector)
            .next()
            .expect("Could not load the price");
        let crypto_price = crypto_price_element.text().collect::<String>();

        let crypto_24_change_element = element
            .select(&crypto_24_change_selector)
            .next()
            .expect("Could not load the 24 HR change");
        let crypto_24_change = crypto_24_change_element.text().collect::<String>();

        let crypto_24_vol_element = element
            .select(&crypto_24_vol_selector)
            .next()
            .expect("Could not load the 24 HR vol");
        let crypto_24_vol = crypto_24_vol_element.text().collect::<String>();

        let crypto_marketcap_element = element
            .select(&crypto_marketcap_selector)
            .next()
            .expect("Could not load the 24 HR vol");
        let crypto_marketcap = crypto_marketcap_element.text().collect::<String>();

        wtr.write_record([&crypto_name, &crypto_price, &crypto_24_change, &crypto_24_vol, &crypto_marketcap]).expect("");


        println!(
            "{:?} : {:?} : {:?} : {:?} : {:?}",
            crypto_name, crypto_price, crypto_24_change, crypto_24_vol, crypto_marketcap
        );
    }
}
