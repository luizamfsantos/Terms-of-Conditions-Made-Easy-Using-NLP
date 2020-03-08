from flask import Flask, render_template, request, flash
from multi_rake import Rake

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hg6h8sg96hds85j'


@app.route("/", methods=['POST', 'GET'])
def home():
    score = 0
    results_score = ''
    results_feedback = ''
    reaction = ''
    temp = ''
    temp2 = ''
    terms_form = ''
    res_good = []
    res_bad = []
    bad_words = {
        "proprietary notice language": 0,
        "reasonable attorneys’ fees": 0,
        "assume total responsibility": 0,
        "communication line failure": 0,
        "attorneys’ fees": 0,
        "similar fees": 0,
        "applicable prices": 0,
        "publicly displayed": 0,
        "manipulate identifiers": 0,
        "losses incurred": 0,
        "injuries caused": 0,
        "irreparable harm": 0,
        "computer virus": 0,
        "apple’s failure": 0,
        "apple’s control": 0,
        "governmental request": 0,
        "out-of-pocket expenses": 0,
        "oral agreements": 0,
        "destructive features": 0,
        "punitive damages": 0,
        "monetary damages": 0,
        "third-party applications connected": 0,
        "re-export control laws": 0,
        "modified additional terms": 0,
        "stop providing services": 0,
        "expressly override": 0,
        "constantly changing": 0,
        "non-exclusive license": 0,
        "remove functionalities": 0,
        "apply retroactively": 0,
        "alleged infringing material": 0,
        "affiliated companies": 0,
        "manual process": 0,
        "mail lists": 0,
        "reverse engineer": 0,
        "trade secret": 0,
        "accounting fees": 0,
        "lost data": 0,
        "external websites": 0,
        "fully responsible": 0,
        "password information": 0,
        "post advertisements": 0,
        "conditions waive": 0,
        "remove communications": 0
    }

    good_words = {
        "intellectual property rights": 0,
        "account information secure": 0,
        "completely private": 0,
        "good faith": 0,
        "accessible worldwide": 0,
        "equitable relief": 0,
        "relief granted": 0,
        "competent jurisdiction": 0,
        "reasonable time": 0,
        "copyrights rights": 0,
        "information secure": 0,
        "apple’s liability": 0,
        "reasonable advance notice": 0,
        "party beneficiary rights": 0,
        "open source license": 0,
        "open source software": 0,
        "legal notices displayed": 0,
        "safety laws": 0,
        "password confidential": 0,
        "malware detection": 0,
        "privacy policy": 0,
        "worldwide license": 0,
        "submit feedback": 0,
        "reasonable requests assisting": 0,
        "good faith belief": 0,
        "limitation security-related features": 0,
        "legally binding agreement": 0,
        "license rights granted": 0,
        "copyright owner's behalf": 0,
        "license includes access": 0,
        "royalty-free license": 0,
        "confidential information": 0
    }

    rake = Rake()

    if request.method == "POST":
        terms_form = request.form.get("input")
        kw = rake.apply(terms_form)
        for word in kw:
            if word[0] in good_words:
                good_words[word[0]] += 1
                res_good.append(word[0])
            if word[0] in bad_words:
                bad_words[word[0]] += 1
                res_bad.append(word[0])

        score = round(
            len(res_good) / (len(res_good) + len(res_bad)) * 175, 2)
        results_score = "The score is {}%".format(score)

        if 0 <= score <= 50:
            results_feedback = "Poor"
        elif 50 < score <= 65:
            results_feedback = "Average"
        elif 65 < score <= 80:
            results_feedback = "Good"
        elif 80 < score <= 100:
            results_feedback = "Excellent"

        temp = ", ".join(res_good)
        temp2 = ", ".join(res_bad)

    return render_template('index.html', results_score=results_score, results_feedback=results_feedback, reaction=reaction, output=temp, output2=temp2)


if __name__ == '__main__':
    app.run(debug=True)
