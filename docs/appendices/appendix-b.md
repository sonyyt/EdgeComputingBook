(appendix-b)=

# Appendix B. Optional Extension: Learning and Adaptation Across Devices

Chapters 10–12 begin with available models and include optional, small-scale training and adaptation experiments. This appendix extends {ref}`Section 11.10 <section-11-10>` into a design exercise for learning across devices. Nevertheless, an edge application may eventually encounter a new room layout, a different device, or a changing data distribution. The systems question is how to detect and manage that change without confusing model adaptation with every other kind of software update.

Begin with the simplest explanation. A shifted temperature distribution may reflect a moved sensor, a changed sampling schedule, a calibration fault, or a genuinely different environment. Retraining a model cannot establish which explanation is true. Verify data provenance and measurement conditions before treating every disagreement as a learning problem.

(appendix-b-b-1-adaptation-without-training)=

## B.1 Adaptation without training

Many useful changes do not require updating model weights. The application may adjust a retrieval window, select a different existing model, revise a prompt, update a deterministic rule, or calibrate a sensor. Each change has a version and an evaluation obligation. A prompt modification that changes the meaning of a generated report should not be hidden behind an unchanged application version.

Use a held-out task set and record the old and new configurations. Roll out a change to a limited deployment, monitor relevant errors and resource use, and preserve a rollback route. This is the same lifecycle discipline discussed for executable components. The model is one stateful dependency among several, not an isolated artifact whose replacement cannot affect the surrounding system.

(appendix-b-b-2-federated-learning-as-a-coordination-pattern)=

## B.2 Federated learning as a coordination pattern

Federated learning coordinates training across participants while leaving their raw training data at those participants. A central coordinator can distribute a model, select clients, collect updates after local training, and combine them into a new model. Federated averaging is a foundational example of this pattern. [{ref}`34 <ref-34>`]

For a simplified round, client $i$ returns parameter vector $w_{i}$ after training on $n_{i}$ examples. A sample-weighted combination is



$$
w_{new} = \frac{\sum_{i}^{}n_{i}w_{i}}{\sum_{i}^{}n_{i}}.
$$



With two scalar toy updates, $w_{1} = 2$ from 10 examples and $w_{2} = 6$ from 30 examples, the result is $(10 \cdot 2 + 30 \cdot 6)/40 = 5$. This arithmetic illustrates aggregation, not a general convergence guarantee. Real training has initialization, optimizer state, multiple local steps, and heterogeneous data distributions.

The edge-systems issues are immediate. Clients have different availability, bandwidth, compute, and power. Waiting for every selected client may delay a round. Ignoring slower clients changes whose data influences the result. Scheduling more local work can reduce communication frequency while changing optimization behavior. These trade-offs require a model-quality measure as well as a resource measure.

(appendix-b-b-3-non-identical-data-and-partial-participation)=

## B.3 Non-identical data and partial participation

Room data need not be independent and identically distributed across devices. One room may be occupied regularly, another rarely; one sensor may have a systematic offset. Averaging updates does not erase these differences. A model that performs well on the pooled dataset may serve a minority of rooms poorly.

Report performance by relevant deployment group where the data and privacy policy permit it. Distinguish a global improvement from an improvement concentrated in frequently participating clients. Personalization may be appropriate, but it creates more artifacts to manage, evaluate, and recover. The application must know which model version belongs to which device or group.

Participation also creates a sampling process. A battery-limited device that trains only while charging may contribute observations from particular times or conditions. Treat availability as a source of possible bias rather than a purely random systems inconvenience. A resource scheduler can therefore influence the learning result even without changing the aggregation equation.

(appendix-b-b-4-privacy-and-security-do-not-follow-automatically)=

## B.4 Privacy and security do not follow automatically

Keeping raw data local reduces one form of direct transfer, but updates can still contain information about local examples. Secure aggregation can protect individual client updates from direct inspection by the aggregator under a specified protocol and threat model. It does not by itself establish differential privacy, prevent malicious training behavior, or prove that the final model reveals nothing sensitive. [{ref}`35 <ref-35>`]

Differential privacy adds a formal, parameterized way to bound information disclosure under its assumptions. Evaluating a claim requires knowing the protected unit, neighboring-dataset definition, parameters, composition, and implementation. A statement that a training process is merely “federated” supplies none of those details. [{ref}`36 <ref-36>`]

A compromised participant can also submit a harmful update or misrepresent its data. Authentication identifies who submitted an update; it does not establish that the update is beneficial. Robust training and malicious-client defenses are advanced topics. The core lesson is to specify the threat model before claiming that decentralization solves trust.

(appendix-b-b-5-suggested-extension-exercise)=

## B.5 Suggested extension exercise

Simulate several clients with different data distributions and participation rates. Compare centralized training on permitted pooled synthetic data, a simple federated scheme, and a no-training baseline. Record communication, completion time, global quality, and per-client quality. When using a lightweight non-language-model task, explain why it is a convenient experimental vehicle rather than implying that its result automatically transfers to LLM adaptation.

Identify an effect of heterogeneity or scheduling that a uniform simulation hides. Document the network payload and distinguish implemented privacy guarantees from intended ones.

