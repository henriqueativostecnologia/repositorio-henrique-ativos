---
fonte: https://help.asana.com/s/article/asana-ip-address-ranges-and-hostnames?language=en_US
baixado: 2026-11-10
---

# Asana IP address ranges and hostnames

This article explains how Asana uses IP addresses and hostnames, and how your network or security team can safely allow access to Asana.

It is written for admins, IT, and security teams who manage firewalls, secure web gateways, or other network controls for people using Asana.

## Does Asana provide a fixed list of IP address ranges?

Asana does not publish a fixed list of IP address ranges for you to allowlist. Asana uses modern cloud infrastructure and content delivery networks. The underlying IPs can and do change over time as our providers operate and optimise their services.

Because of this, relying on individual IP addresses is brittle. Rules that are pinned to a small set of IPs can start blocking traffic when the infrastructure behind Asana changes. A hostname based approach is more stable and easier to maintain.

## Recommended approach to allow access to Asana

The recommended way to control access to Asana is to allow traffic based on DNS hostnames, over HTTPS, with certificate validation. When you allow outbound HTTPS to the Asana domains listed below, your users can sign in and work in Asana while your existing security controls continue to apply.

In most cases, you should:

1.  Allow outbound HTTPS traffic to the documented Asana hostnames.
2.  Rely on TLS certificate validation to make sure clients connect securely to Asana services.
3.  Avoid pinning rules to a small, static set of IP addresses wherever possible.

If your organisation must maintain IP based firewall rules, your IT or security team can consult the public IP documentation from our cloud providers, such as AWS, and combine that information with the hostname lists below. Because those IP ranges are owned and updated by the providers, Asana cannot guarantee or maintain IP lists on your behalf.

For more detail on how Asana protects your data, you can review our security, privacy, and compliance documentation in the [Asana Trust Center](https://trust.asana.com/).

## Domains to allowlist for non FedRAMP environments

For non FedRAMP customers, Asana currently recommends allowlisting the following domains for full product use, including attachments and avatars:

1.  asana.com
2.  \*.asana.com
3.  \*.asana.plus
4.  asanausercontent.com
5.  d3ki9tyy5l5ruj.cloudfront.net
6.  asana-user-private-us-east-1.s3.amazonaws.com
7.  asana-user-private-me-central-1.s3.me-central-1.amazonaws.com
8.  asana-user-private-ap-northeast-1.s3.ap-northeast-1.amazonaws.com
9.  asana-user-private-eu-central-1.s3.eu-central-1.amazonaws.com
10. asana-user-private-ap-southeast-2.s3.ap-southeast-2.amazonaws.com

These domains cover the core web application, APIs, file uploads and downloads, avatars, and our global content delivery network.

If you know which Asana data region your organisation uses, you can optionally scope S3 specific rules to just the bucket that matches your region and omit the others. If you are not sure which region you are in, allowing all of the listed S3 buckets is the safest option.

## Domains to allowlist for FedRAMP environments

For customers using Asana in our FedRAMP environment, Asana recommends allowlisting these domains:

1.  app.asana-gov.com
2.  asana-user-private-fedramp-prod.s3.amazonaws.com
3.  asanausercontent.com
4.  d1dg3ns82tdjz3.cloudfront.net

At the time of writing, asanausercontent.com is not yet used in FedRAMP, but content may be served from this domain in the future. Including it in firewall rules now reduces the risk of future access issues when that change happens.

## Other domains you might see

Depending on how your users work with Asana, you may also see traffic to third party services that integrate with Asana, such as Google, Microsoft, Dropbox, or Box. For example, attaching a file from Google Drive or OneDrive requires access to those providers.

Your organisation should decide how to manage access to third party services as part of your wider security posture. Asana does not control or publish IP address lists for those external providers.

## Why we do not recommend IP based allowlists for Asana

IP based firewall rules can be appropriate in some environments, but they are not the most reliable way to manage access to Asana. Asana runs on cloud infrastructure that automatically scales and shifts traffic. That means the set of IPs used to serve Asana can change over time.

If you pin your allowlist to a small set of static IPs, your users can lose access when the infrastructure behind Asana changes. Investigating and updating those rules often takes longer than adjusting hostname based controls.

Hostname based rules are more stable because they follow DNS. As our infrastructure evolves, DNS continues to point your clients to the correct endpoints, while your firewall rules still check that traffic is going to the domains you approved.

If your security policies require IP based controls, we recommend combining hostname based rules with the cloud provider documentation your team already uses, and reviewing those IP based controls regularly.

## Frequently asked questions

### Can Asana send us a list of IP addresses to allowlist?

Asana does not provide a static list of IP addresses for you to allow. The infrastructure that serves Asana changes over time, so any static IP list would quickly become inaccurate and could lead to service interruptions. Instead, we recommend allowing access based on the Asana hostnames listed above.

### Are there customer specific IP addresses or domains?

No. Asana does not allocate customer specific IP address ranges or hostnames. Multiple customers share the same infrastructure and domains.

### Do these domains cover APIs, mobile apps, and attachments?

Yes. The recommended domains cover the core web application, APIs, mobile apps, and access to attachments and avatars. If your organisation uses additional integrations or third party services, you may need to allow those providers separately.

### What if our security team needs more detail?

If your security team has detailed questions about the domains listed here, your Asana account team or support contact can work with you. They can confirm the latest guidance from our Infrastructure and Security teams and help you understand how it applies to your environment.

Your team can also review our documentation in the [Asana Trust Center](https://trust.asana.com/).
