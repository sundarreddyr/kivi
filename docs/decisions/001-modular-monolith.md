# 001 — Start with a modular Quarkus application

Status: accepted for the skeleton.

The owner chose Java and Quarkus for household workflows. Use Maven, Java 21 and one application depending on a plain Java kitchen module. These are reversible starting defaults. MySQL is the intended first record store; defer migrations and entities to the modelling milestone.

A separate Python service would add a deployment boundary before a distinct runtime requirement exists. Offline experiments can use Python independently. Revisit extraction as a service if a measured workload requires separate scaling or local inference hardware.
