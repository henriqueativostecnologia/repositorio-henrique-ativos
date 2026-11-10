---
fonte: https://support.google.com/appsheet/answer/10104800?hl=en
baixado: 2026-11-10
---

# Predictive models

This feature is available to **AppSheet Enterprise Plus **accounts only. See [What features are supported with each subscription?](https://support.google.com/appsheet/answer/10105400#features)

Predictive models perform a statistical analysis of your app data in order to make predictions about future data. Some examples include:

- **Categorizing customer feedback**, given examples of feedback and the categories they belong to
- **Predicting customer churn**, given examples of customers and whether they churned
- **Estimating the cost of a project**, given examples of previous projects and how much they cost

Predictive models work by using machine learning algorithms to generalize from your historical data. Machine learning has two phases:

- The **training phase**, when your historical **training data** is analyzed and a new predictive model is created
- The **prediction phase**, when your predictive model makes **predictions** on data that was not included in your training data

**About Google Machine Learning**

Behind the scenes, AppSheet uses Google Cloud's Machine Learning Platform to create predictive models. This means that during the training phase, your data is accessed by AppSheet's code running on a Google Cloud service. During the prediction phase, your model is privately hosted on another Google Cloud service.

Use predictive models as described in the following sections:

- [Get started](#get-started)
- [Create a new predictive model](#create)
- [Model training](#model-training)
- [Make predictions](#make-predictions)

## Get started

Watch a video to learn more about creating predictive models.

**Note**: The concepts in this video are still valid, though the AppSheet app editor UI has changed since it was recorded.

Video: https://www.youtube.com/watch?v=-cw7UmeAeL4

## Create a new predictive model

To create a predictive model:

1.  Open your app in the editor.

2.  Go to **Intelligence ** Intelligence icon .
    The Intelligence panel opens.

3.  Click **+** adjacent to the **Predictive Models** heading.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to the **Intelligence \> Predictive Models** pane and click **+ New Predictive Model**.

4.  Rename the predictive model by updating the **Model** **Name** field.

5.  Configure the training model, including:

    - **Training Data Table**: This is the table in your app that holds your historical data that is used as input to the machine learning algorithm.
    - **Column To Predict:** The column in your training data that you want to make future predictions about. The column to predict must be `Yes/No`, `Enum`, `Ref`, `Price`, `Decimal`, or `Number`.
    - **(Optional) Model Inputs:** The columns in your training data that contain relevant information for making a prediction. If this is left blank, AppSheet will automatically infer which columns are relevant. If you need to override AppSheet's decision, then you can explicitly specify the relevant columns.

6.  Save the app.

## Model training

Once the editor refreshes, you will be shown a live status of your model as it is being trained. Training generally takes less than a minute, but depends on the size of your training data.

Preparing training data message in the Model Summary section

Once your model has finished training, you will be shown feedback about your model's accuracy and information about how it makes predictions. The particular information shown will depend on the type of column that your model is predicting.

Shows results of predictive model training under Model Summary

## Make predictions

Once your model is trained, you can incorporate it into your app in a few different ways. The easiest way to use your model is to flip a switch in your model's configuration that will do one of the following:

- Add a virtual column to your table that will hold your model's output prediction
- Add an initial value to your prediction column

Use your model section of the Predictive Model configuration

You can also use the `PREDICT("Your Model Name Here")`  formula to incorporate your model's predictions in other parts of your app.
