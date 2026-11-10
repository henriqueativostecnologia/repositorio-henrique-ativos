---
fonte: https://support.google.com/appsheet/answer/15999115?hl=en
baixado: 2026-11-10
---

# Limits and limitations with AI in automations

The following sections describe the limits, limitations, and credits for AI in automations.

- [Limits](#limits)
- [Limitations](#limitations-known-issues)

## Limits

Consider the following limits when using AI in automations.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Item**                                                                      | **Limit**                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum data type sizes supported when using AI in automations                | `Image`: 5 MB\                                                                |
|                                                                               | `File`: 12 MB                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of queries per minute                                          | 30 (approximately)                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Maximum number of records to fetch via AI tasks: Extract rows and Categorize  | 50                                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Limitations

It is important to understand the limitations with AI in automations, specifically when extracting information from images and PDF documents. These limitations might change in the future; we recommend checking back to this page periodically.

### Images

Here are some issues that generative AI models are known to struggle with when processing images:

- Reading an analog measurement device
- Extracting information from low-resolution, rotated, or poor quality images
- Extracting information from images that violate our safety policies
- Identifying people that aren't celebrities 
- Counting objects

### PDF documents

The following use cases for PDF document extraction might produce unexpected results:

&nbsp;

- Counting objects
- Images within a PDF document may not be processed properly; small images relative to the size of the PDF are more likely to have processing issues
