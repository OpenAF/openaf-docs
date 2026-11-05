---
layout: default
title: oafp with OpenAI
parent: oafp
grand_parent: Guides
---

# oafp with OpenAI

Choose a model enabled for your account and replace the placeholders below. The sample output illustrates formatting; model-generated factual data must be checked independently. See [provider configuration](../../concepts/llm.md).

List of examples of use of oafp using OpenAI's ChatGPT models:

### Setting up the LLM model and gather the data into a data.json file

```bash
export OAFP_MODEL="(type: openai, model: YOUR_MODEL_ID, key: YOUR_API_KEY, timeout: 900000)"
echo "list all United Nations secretaries with their corresponding 'name', their mandate 'begin date', their mandate 'end date' and their corresponding secretary 'numeral'" | oafp input=llm output=json > data.json
```

Result:

```
oafp data.json
─ secretaries ╭ [0] ╭ name      : Trygve Lie
              │     ├ begin date: 1946-02-01
              │     ├ end date  : 1952-11-10
              │     ╰ numeral   : 1
              ├ [1] ╭ name      : Dag Hammarskjöld
              │     ├ begin date: 1953-04-10
              │     ├ end date  : 1961-09-18
              │     ╰ numeral   : 2
              ├ [2] ╭ name      : U Thant
              │     ├ begin date: 1961-11-30
              │     ├ end date  : 1971-12-31
              │     ╰ numeral   : 3
              ├ [3] ╭ name      : Kurt Waldheim
              │     ├ begin date: 1972-01-01
              │     ├ end date  : 1981-12-31
              │     ╰ numeral   : 4
              ├ [4] ╭ name      : Javier Pérez de Cuéllar
              │     ├ begin date: 1982-01-01
              │     ├ end date  : 1991-12-31
              │     ╰ numeral   : 5
              ├ [5] ╭ name      : Boutros Boutros-Ghali
              │     ├ begin date: 1992-01-01
              │     ├ end date  : 1996-12-31
              │     ╰ numeral   : 6
              ├ [6] ╭ name      : Kofi Annan
              │     ├ begin date: 1997-01-01
              │     ├ end date  : 2006-12-31
              │     ╰ numeral   : 7
              ├ [7] ╭ name      : Ban Ki-moon
              │     ├ begin date: 2007-01-01
              │     ├ end date  : 2016-12-31
              │     ╰ numeral   : 8
              ╰ [8] ╭ name      : António Guterres
                    ├ begin date: 2017-01-01
                    ├ end date  : present
                    ╰ numeral   : 9
```

```
oafp data.json path=secretaries output=ctable
         name          │begin date│ end date │numeral
───────────────────────┼──────────┼──────────┼───────
Trygve Lie             │1946-02-01│1952-11-10│1
Dag Hammarskjöld       │1953-04-10│1961-09-18│2
U Thant                │1961-11-30│1971-12-31│3
Kurt Waldheim          │1972-01-01│1981-12-31│4
Javier Pérez de Cuéllar│1982-01-01│1991-12-31│5
Boutros Boutros-Ghali  │1992-01-01│1996-12-31│6
Kofi Annan             │1997-01-01│2006-12-31│7
Ban Ki-moon            │2007-01-01│2016-12-31│8
António Guterres       │2017-01-01│present   │9
[#9 rows]
```
