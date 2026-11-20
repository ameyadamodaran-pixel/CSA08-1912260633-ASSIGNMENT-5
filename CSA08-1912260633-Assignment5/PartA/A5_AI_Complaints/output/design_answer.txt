# A5 — AI Application Design for Citizen Complaints (4 marks)

## Sentiment and summary
Use a small word-list sentiment scorer: positive terms add +1, negative terms −1, and a preceding negation word flips the next sentiment word. Extractive summary: split into sentences, score by frequency of informative words, and return the top sentence(s). It is transparent and lightweight but misses context, sarcasm, spelling variation and domain meanings.

## Rule-based chatbot
Match terms such as `PM2.5`, station name and `today`/date, then query SQLite with placeholders. It can answer only supported patterns and may not understand paraphrases or follow-up context.

## Alternative ML model
A trained model may improve language coverage but requires labelled training data, model memory and inference time, and can make less transparent predictions. A lexicon is fast, small and explainable; validate agreement on a labelled sample before deciding whether ML is justified.
