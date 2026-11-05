(appendix-c)=

# Appendix C. Selected Exercise Solutions

(appendix-c-c-1-chapter-1)=

## C.1 Chapter 1

**1.1.** A camera can produce an image, execute a counting task, and produce a timestamped count. Device-side execution sends selected results onward; remote execution transfers the input needed by the remote task. The drawing must identify the actual computation, not just the presence of a local gateway. Other applications can give equally valid answers. One shared functional requirement is to display a timestamped count. Two illustrative non-functional requirements are a response within 200 ms and retention of raw images inside the premises; the latter can rule out an otherwise functionally valid remote design.

**1.2.** One billion parameters at two bytes each occupy 2 billion bytes, or 2 decimal GB, for parameter values alone. Runtime code, intermediate results, request state, and other processes require additional working memory. Storage capacity does not automatically provide that RAM, and a model’s total running footprint cannot be inferred from its file size alone.

**1.3.** Classification executes on the shop server; cloud installation and updates are management functions. A link outage can stop new updates without stopping already available local inference. Further checks include local availability of the model, identity validation, configuration, and access to input data.

**1.4.** The changed site budget is $20 + 10 + 150 + 35 = 215$ ms. Doubling the cloud network contribution yields $20 + 160 + 30 + 15 = 225$ ms. With both changes, only the original 140 ms on-device path meets the assumed 200 ms target. These are assumed budgets; actual workload, queueing, hardware, and model quality must still be measured.

**1.5.** The original sensors produce 24.8832 MB/day, so a 50% reduction saves 12.4416 MB/day. One assumed video stream produces 21.6 GB/day, saving 10.8 GB/day at 50%. The retained information, installation cost, privacy requirements, and disconnected behavior can matter more than either percentage.

**1.6.** A photograph can establish visible form, connections, and installation context. It does not by itself establish where the application executes, available capacity, network route, ownership, or operational status. A proposed architecture must label those inferences rather than present them as observed facts.

**1.7.** An hourly environmental report may prioritize battery life and communication coverage; interactive image classification may prioritize response time and sufficient compute. A local or remote design is acceptable when the stated constraints support it. A useful experiment varies a condition that could reverse the choice, such as uplink availability or shared-server load.

**1.8.** A valid drawing separates local sensing, data storage, model inference, and any remote management or optional analysis. For an operation to survive a cloud-link outage, its local artifacts, permissions, working resources, and user path must remain available. A local-looking screen alone is not evidence that these dependencies are local. Uploading a permitted summary is a data transfer; choosing to run inference on the site server is a computation-placement decision; assigning memory or adding a worker is a resource-allocation decision. They change different parts of the design.

**1.9. One possible comparison is CDN content delivery and VM-based cloudlets. A CDN moves stored content closer to users to reduce repeated origin trips; a cloudlet offers nearby execution for resource-intensive mobile tasks. Neither automatically establishes privacy, sufficient capacity, or continued operation under all failures. They differ in the work performed: serving an existing object versus computing a new result from an input. Other pairings supported by {ref}`Table 1.4 <table-1-4>` are also valid.**

**1.10. The parameter ratio is 4.2 / 138 ≈ 0.0304 (about 1/33); the multiply-add ratio is 569 / 15,300 ≈ 0.0372 (about 1/27). Reported accuracy changes by 70.6 − 71.5 = −0.9 percentage points. Neither count ratio measures device latency. An example estimate is the 18.5 billion IoT connections for 2024, which does not count proven edge deployments. An example forecast is IDC’s approximately US\$450 billion spending in 2029, which is not realized spending. An experimental result is the reported MobileNet ImageNet accuracy, which does not establish accuracy or response time for an unrelated course application.**

(appendix-c-c-2-chapter-2)=

## C.2 Chapter 2

**2.1.** Changing five-minute bins to ten-minute bins changes a parameter. Adding an occupancy filter introduces another input and join dependency. A user-defined rolling-median event introduces a new calculation. A flexible implementation must alter the affected computation while retaining the original access scope and unaffected assumptions.

**2.2.** The data-access service or checked tool boundary rejects the unauthorized room. The model may explain the limitation or offer analysis within the authorized scope; it cannot authorize itself. A tool-call message is a proposal until the runtime executes it and receives an outcome.

**2.3.** Units determine the meaning of the difference threshold; observation time determines rolling windows and duration; quality determines which observations may support the calculation; the catalog tells the planner whether the needed fields and history exist. Device, boot, and sequence primarily identify logical events for ingestion. A room field describes scope but is not a verified identity or permission token.

**2.4.** The five-minute bin has three valid observations out of five known-occupied opportunities: 60%, below 80%. Its arithmetic mean is 23.55°C but is omitted under the rule. The ten-minute bin has eight of ten: 80%, which is accepted; the mean is 23.7375°C. Changing aggregation changes the evidence unit, not the earlier rule’s correctness.

**2.5.** With the repair, the request takes $5.80 + 1.50 = 7.30$ seconds. With only the three extra round trips, it takes $5.80 + 3(0.12) = 6.16$ seconds. Both exceed 6 seconds; the original 5.80-second budget meets it. A real remote model may change compute time, task quality, and the number of interactions, invalidating an otherwise-equal assumption.

**2.6.** Coverage is $18/20 = 90\%$. Correctness among answered tasks is $16/18 \approx 88.9\%$. Overall successful completion is $16/20 = 80\%$. A changed grouping window and a novel combination of occupancy filtering with an event definition are useful held-out changes. Invalid or unauthorized tasks need their own expected handling, not inclusion as ordinary answerable questions.

**2.7.** Annual hardware allocation is 200, energy is 35.04, and maintenance is 40, totaling 275.04 cost units. At 3,650 and 36,500 yearly requests, the allocated unit costs are approximately 0.0754 and 0.00754. A remote design must account for retained site equipment, service charges, networking, and relevant operations. A data-release restriction or required offline function can exclude a nominally cheaper option.

**2.8.** Observe a new request while the wide-area link is unavailable, verify local model and tool activity, and check a newly computed output against the local data. A cached answer or stub trace is insufficient. This observation still does not establish all restart conditions, multi-user isolation, sandbox security, or general model quality.

(appendix-c-c-3-chapter-3)=

## C.3 Chapter 3

**3.1.** A phone is a device class; an accelerometer is a sensing modality/component; activity recognition is an application task. One device can expose several modalities and support several tasks. A smartphone can be a data source, a gateway, or an inference host, but its role does not redefine the sensor physics.

**3.2.** Three 16-bit axes produce $3 \cdot 2 \cdot 50 = 300$ bytes/s, or $300 \cdot 28,800 = 8,640,000$ bytes in eight hours. Adding one eight-byte timestamp to each three-axis sample makes the rate $(6 + 8) \cdot 50 = 700$ bytes/s and storage 20,160,000 bytes. Framing, metadata, checksums, indexes, and compression are not included. This is a payload model, not a phone battery estimate.

**3.3.** Repeated averaging can reduce some zero-mean random noise but does not remove a fixed calibration offset. Estimate the offset against a suitable reference, report the correction and uncertainty, and test over the relevant operating conditions. Do not infer higher physical accuracy merely from more decimal places.

**3.5.** The displacement scale is $12\, m/s \times 0.040\, s = 0.48$ m. This is the error contribution of the assumed time offset under constant motion, not the complete localization error. Correct timestamps and transforms, estimate their uncertainty, and account for motion during acquisition.

(appendix-c-c-4-chapter-4)=

## C.4 Chapter 4

**4.1.** Wi-Fi is an access/link technology; IP supplies network addressing and forwarding; TCP supplies a reliable ordered byte stream; MQTT defines an application messaging exchange. Thread supplies an IP-based low-power mesh stack, while Matter adds application interoperability. These can be complementary rather than interchangeable; choose complete stacks with compatible interfaces.

**4.2.** At five observations/s, individual messages carry $5(12 + 36) = 240$ bytes/s, or 1,920 bits/s. One batch of five each second carries $5 \cdot 12 + 36 = 96$ bytes/s, or 768 bits/s: a 60% reduction in this simplified byte budget. If a batch is sent immediately when its fifth observation arrives, the oldest waits 0.8 s. The answer excludes radio scheduling, loss, and connection setup.

**4.3.** A protocol acknowledgment belongs to its specified exchange. It does not automatically prove that the subscriber has committed its database transaction or that a physical action completed. Specify the application result, stable identity, durable state, and retry behavior separately.

**4.4.** An IP border router connects networks and forwards compatible IP traffic; it does not by itself translate device attributes into a shared application meaning. Semantic interoperability additionally needs agreed data models, units, operations, discovery, and authorization. A bridge that translates those meanings adds a distinct trust and state boundary.

**4.5.** For a device that can receive only during infrequent receive windows, a 500 ms downlink requirement may be infeasible even when the radio offers sufficient throughput. Check the maximum wait for a receive opportunity, network scheduling, retransmissions, and wake/processing time. Either revise the mode or requirement, or retain the time-critical decision locally; do not infer a deadline guarantee from a nominal bit rate.

4.7. The scene supplies presentation and possibly structural geometry. A current-state question additionally needs identified equipment, source-to-property mapping, an observation/update path, and timestamps/quality with a freshness rule. A new rendering alone does not create new observations.

4.8. Accept unique observations 101, 103, and 102; the second 103 is a duplicate, while its altered version is a conflict. Latest state stays 46 °C at 10:00:04. At 10:00:11 its age is 7 s, exceeding the assumed 5 s threshold. This uses comparable clocks; uncertain clock offset requires qualification.

4.9. Starting at 40 °C: step 1 is 40 + 0.2(25 − 40) + 2 = 39 °C; step 2 is 39 + 0.2(25 − 39) + 2 = 38.2 °C. Actual validation would require independent temperature trajectories under stated ambient/load conditions and evidence about sensor accuracy and whether the coefficients transfer across the intended operating range. Arithmetic agreement alone is insufficient.

4.10. Desired configuration is not reported configuration. Show both versions/values with request and observation times, and mark application as pending or unconfirmed. Reloading a stored page changes its display time, not the age of its physical evidence.

(appendix-c-c-5-chapter-5)=

## C.5 Chapter 5

**5.1.** Put application code and its declared runtime dependencies in the distributable package. Keep mutable history in explicitly managed persistent storage; supply device-specific configuration separately. A cloud credential is neither ordinary source code nor public image content: grant only the required access and deliver it through an appropriate protected mechanism. Model artifacts may be distributed separately when size or update frequency makes that useful, but the deployment must still identify the exact artifact and its availability.

**5.2.** An image built only for x86-64 does not become an ARM image merely because both hosts run Linux. Check processor architecture, host/kernel requirements, dependencies, and any device or accelerator interfaces. Build a compatible image variant or use an explicitly supported translation strategy, then validate behavior on the target. Portability of source, binaries, and performance are different claims.

**5.3.** After reserving 3 GiB, the application budget is 5 GiB. At the assumed 2 GiB per worker, two workers fit arithmetically, leaving 1 GiB within that budget. Three require 6 GiB and do not fit. Real transient allocations, shared services, and accelerator memory may require a more conservative concurrency setting; this arithmetic is not a response-time guarantee.

**5.4.** Different container filesystems do not create separate physical processors, memory, storage bandwidth, or power supplies. Resource limits and admission rules can reduce interference, while application permissions determine which data and operations each user can access. All containers on one host still share important failure boundaries.

(appendix-c-c-6-chapter-6)=

## C.6 Chapter 6

**6.1.** At the assumed target utilization, each worker contributes $8 \times 0.6 = 4.8$ requests/s of planned capacity. The replica count is $\lceil 12/4.8\rceil = 3$. This model assumes independent requests and enough underlying resources. It does not establish a percentile latency or eliminate shared database and network bottlenecks.

**6.2.** A stateless analyzer whose request contains the necessary input is easier to replicate than a collector that owns a device subscription or a service with an in-memory user session. Replicating the latter requires a deliberate design for ownership, shared state, duplicate processing, and routing. Separate those concerns before interpreting replica count as capacity.

**6.3.** Three replicas on one node provide three execution instances, not three machines or three independent failure domains. They may still be useful if the host has spare capacity, but share its hardware and compete for resources. Observe actual placement and resource use, not only the requested replica count.

**6.4.** Creating five additional Pods does not create five additional machines. If no existing node satisfies their requests and constraints, they can remain pending. Node provisioning requires a separate supported mechanism and available capacity; a fixed classroom cluster cannot manufacture more physical hardware.

**6.5.** A frequently used model with expensive loading may benefit from resident capacity. A short report requested once per day may benefit from on-demand execution. Compare startup time, reuse frequency, memory residency, state dependencies, and management cost. “Serverless” alone does not show that either workload meets its deadline or costs less.

(appendix-c-c-7-chapter-7)=

## C.7 Chapter 7

**7.1.** At 100 Mb/s, uploading 2 decimal MB takes $16/100 = 0.16$ s, or 160 ms. Adding the assumed 30 ms fixed communication, 40 ms waiting, 60 ms execution, and 4 ms return gives 294 ms, below 350 ms locally. For the proposed 0.1 MB representation, transmission takes 8 ms; with 20 ms local preprocessing, the total is $20 + 8 + 30 + 40 + 60 + 4 = 162$ ms. This second comparison is meaningful only if the representation supports the required result and its release is permitted.

**7.2.** Means and extrema can conceal temporal order, short events, and relations between signals. Retain the information needed by the supported task, not simply the smallest record. Two histories with the same mean can differ in whether a change preceded or followed occupancy.

**7.3.** Desired version 8 records intent; reported version 7 records the last confirmed applied state. Do not display version 8 as running until the device has applied and reported it under the protocol. Include timestamps and uncertainty when the device is disconnected or reports are delayed.

**7.4.** A lost acknowledgment cannot tell the sender whether the receiver committed the event. Keep a stable logical event identifier across retries, retain a durable pending record until acknowledgment, and make receiving the same event again duplicate-safe. A conflicting payload under an existing identifier is not an ordinary duplicate and requires a stated policy.

(appendix-c-c-8-chapter-8)=

## C.8 Chapter 8

**8.1.** Increasing a Deployment from two replicas to four changes desired service capacity. Choosing which waiting application request runs next is a different decision. The platform may place the new replicas while an application queue still uses an unchanged request-ordering policy.

**8.2.** When both tasks are waiting, batch-first completes the 200 ms batch at 200 ms and the 40 ms interactive task at 240 ms; the interactive task misses a 100 ms deadline. Interactive-first completes it at 40 ms and the batch at 240 ms. If the non-preemptible batch started 20 ms before the interactive arrival, 180 ms remains, and the interactive response takes 220 ms after its arrival. Reordering the waiting queue cannot interrupt work already executing under this assumption.

**8.3.** A design that sends prohibited raw data to a remote service is infeasible, even when fast or inexpensive. Consider an explicitly permitted representation or local execution; do not assume that removing some fields or generating a feature vector automatically authorizes release.

**8.4.** During an eight-second startup interval, the backlog increases by $(18 - 12) \times 8 = 48$ requests. If capacity then becomes 24 requests/s while arrivals remain at 18, the excess 6 requests/s drains that backlog in eight additional seconds. Capacity of 18 only prevents further growth; it does not drain the accumulated queue. These fluid calculations omit individual service-time variation.

**8.5.** Compare policies using the same task set, offered load, network trace, quality rules, and cost scope. Include startup, transfer, decision overhead, rejected tasks, and failed requests. Report both conditions where adaptation helps and conditions where its overhead or inaccurate measurements make it worse.

(appendix-c-c-9-chapter-9)=

## C.9 Chapter 9

**9.1.** For Greengrass, connect a component’s execution environment to {ref}`Chapter 5 <chapter-5>`, target deployments and lifecycle management to {ref}`Chapter 6 <chapter-6>`, local records and shadow synchronization to {ref}`Chapter 7 <chapter-7>`, and admission or release policy to Chapter 8. For Wavelength, connect EC2 and application packaging, compatible worker replicas and request entry, the Wavelength–Region data path, and placement or capacity policy. Distributing software to multiple targets does not itself route user requests among them.

**9.2.** The interactive critical path includes the phone’s upload, eligible network entry, worker waiting and execution, and result return. A deferrable report can follow a separate regional path. Trace downstream requests, storage reads, and identity dependencies to find whether the supposedly nearby answer still waits for a regional operation.

**9.3.** Distinguish tenant host isolation, VPC/network rules, instance or container resource settings, and application authorization. None alone establishes a response-time target. Increasing service replicas also needs available nodes, compatible placement, a working request entry, and the relevant data path. Describe each layer instead of asserting that a platform’s “multi-tenancy” solves all four.

**9.4.** Put the latency-sensitive service on a suitable Wavelength resource, and place deferrable processing on permitted regional resources. A standard regional Lambda function remains regional; a VPC association does not make it a Wavelength execution environment. Lambda@Edge is a separate CloudFront-associated execution service. A self-managed function runtime on an EC2 worker has its own capacity and operational responsibilities.

**9.5.** A local EKS control plane on an Outpost changes where specified cluster-management functions execute. It does not demonstrate independence from every regional dependency, credential service, image source, or application database. Test the particular operation and disconnection duration, distinguishing already-running work from new deployment and restart.

**9.6.** Under the chapter’s hypothetical assumptions, all-edge requires $\lceil 80/5.6\rceil = 15$ workers. The split needs eight edge and eight regional workers. At edge price 0.60, all-edge costs $15(0.60) = 9.00$ units/h and the split costs $8(0.60) + 8(0.35) + 0.60 = 8.20$ units/h, an 8.9% reduction rather than 18.3%. The break-even additional split overhead is $9.00 - \left\lbrack 8(0.60) + 8(0.35) \right\rbrack = 1.40$ units/h. This exercise is a sensitivity calculation, not a current cloud quotation.

**9.7.** CloudFront Functions does not supply arbitrary request-body access or outbound network calls. Keep permitted header, URL, or cache-key processing at that boundary, and send the image to a suitable regional or near-user application service. That service can call a model under its own data, capacity, and authorization rules; the lightweight function is not thereby performing inference.

**9.8.** Use a declared offered-load pattern, repeated cold and warm requests where relevant, representative inputs, fixed quality checks, and a recorded population of successes, errors, and timeouts. Report a percentile over that population with its sampling limitations, then vary load or connectivity. One warm request cannot establish p95 behavior or future deadline guarantees.

(appendix-c-c-10-chapter-10)=

## C.10 Chapter 10

**10.1. Task metrics**

There are 95 true positives, 5 false negatives, 20 false positives, and 1,880 true negatives. Accuracy is 1,975/2,000 = 98.75%; fault recall is 95%; precision is 95/115 ≈ 82.61%. None establishes the harm of a missed fault or an unnecessary intervention. Timing, class prevalence outside the sample, and thresholds still need application-specific analysis.

**10.2. End-to-end latency**

The baseline takes 130 ms. Halving inference changes 70 ms to 35 ms and produces 95 ms overall, a 35 ms or approximately 26.92% reduction. End-to-end speedup is 130/95 ≈ 1.37, not two. Shortening a motion window may remove the evidence needed to recognize an activity; it is then a task change rather than a free timing improvement.

**10.3. Storage and live tensors**

The raw parameter payloads are 4,800,000, 2,400,000, and 1,200,000 bytes. The feature map occupies 1,605,632 bytes (1.53125 MiB) at FP32. Metadata, scales, biases of another precision, live activations, scratch, runtime and application allocations are additional. Quantizing only weights does not establish activation precision or the actual peak RAM.

**10.4. Mapping and clipping**

The codes are −3, 3, 6, and 127. Reconstructed values are −0.3, 0.3, 0.6, and 12.7. Absolute errors are 0.04, 0.04, 0.04 and 2.3. The first three are within half the grid spacing; the last is outside the representable range and is clipped. These inputs avoid the rounding-rule ambiguity of exact half steps.

**10.5. Evidence of integer execution**

Artificially rounded values used by floating-point operators show a numerical approximation, not integer-kernel performance. Inspect the converted graph/backend and actual operator types, tensor representations, and conversion boundaries. Dynamic quantization determines activation ranges at invocation; static PTQ estimates ranges using representative data before deployment. QAT changes preparation by simulating quantization effects while training, and still requires conversion and actual target execution.

**10.6. Two forms of pruning**

A dense 64 × 64 representation still stores 4,096 weight entries after 2,048 become zero. A sparse file can have different storage, but arbitrary zeros only save executed arithmetic with suitable kernels. Removing 32 output units creates 32 × 64 weights plus 32 biases and removes the corresponding 32 inputs from the next layer. Recovery training and quality checks are necessary; remaining parameter counts alone do not predict wall-clock speed.

**10.7. Distillation controls**

More training steps confound the teacher-guidance effect. Start direct and distilled students from the same initialization, use the same data and minibatch sequence, equal maximum budgets, the same selection rule, and a frozen teacher; choose settings without the test set. Report an unfavorable result rather than repeatedly changing settings on test feedback. In the supplied configuration, the same-size direct student is the stronger measured baseline; this is not a general claim against distillation.

**10.8. Architecture arithmetic**

Standard convolution uses 3² × 32 × 64 = 18,432 multiplications per output location. Depthwise plus pointwise uses 3² × 32 + 32 × 64 = 2,336. The ratio is about 7.89 under matched geometry, excluding biases. These graphs differ; the new architecture needs trained weights and quality evaluation. Kernel support, memory traffic and device utilization determine realized timing.

**10.9. Backend boundaries**

Record operator placement, per-operator execution, transfer/layout-conversion time, synchronization, host/device memory and end-to-end timing. Compare a graph with a compatible substitute for the unsupported operator and a CPU-only baseline that avoids repeated crossings. A third possibility is to retain a larger connected subgraph on one processor. Validate unchanged task meaning and acceptable numerical behavior after every change.

**10.10. Data leakage and updates**

Near-duplicate frames of the same physical object can expose object-specific details across training and testing. Split by object, capture session or site as appropriate, and reserve genuinely later or different conditions for deployment evaluation. Use separate development and held-out sets for update selection; preserve old tasks as regression tests. Labels and acceptance criteria must be reliable, including appropriate permission for using field data.

**10.11. A valid laboratory report**

A report names model and preprocessing artifacts, split and seeds, quality and rejection rules, numeric payload and actual serialized size. It defines whether timing covers one model call, the whole application, or startup. Host CPU timings cannot establish a phone/NPU speedup, a peak-memory saving or lower energy use without corresponding measurements. Predictions and parameter counts are directly reproducible from supplied artifacts; new timing values may differ on another machine.

**10.12. Microcontroller feasibility**

The stated SRAM requirement is 306 KiB, exceeding 256 KiB by 50 KiB. Enough flash for the model does not solve the working-memory shortage. If weights are already read from flash, compressing only those weights does not remove the SRAM allocations. Inspect live activation lifetimes, scratch and buffers, or change the model/input/runtime. Recalculate after an actual compatible transformation instead of subtracting model-file savings from RAM.

(appendix-c-c-11-chapter-11)=

## C.11 Chapter 11

**11.1.**

Replicas mainly change capacity and fault placement; compare throughput and response time while checking identical behavior. Additional views change evidence; compare matched objects/intervals and quality under missing views. Do not attribute evidence gains solely to more processors.

**11.2.**

Offline coverage is 325/360 = 90.28%. Accepted-answer accuracy is 322/325 = 99.08%. The online cascade answers all 360 inputs and has 346/360 = 96.11% accuracy. The populations and coverage differ.

**11.3.**

Correct count changes by rescued minus damaged: 350 + 1 − 5 = 346. Examine branch errors and optional input-quality/label checks using development or validation data. Freeze the new rule before a genuinely new final evaluation; the inherited test set cannot become an unseen holdout again.

**11.4.**

An early-exit network shares computed prefix activations between the branch head and deeper layers. Independent complete classifiers do not share matching intermediate states unless designed to do so. Both may perform similar preprocessing, but that alone does not provide model-prefix reuse.

**11.5.**

45 + 25,088×8/20,000,000×1,000 + 20 + 60 + 10 = 145.0352 ms, above 130 ms. Measure actual tensor formats, transfer/serialization, queueing, backend numerical behavior, and end-to-end output checks.

**11.6.**

The 50% saving compares 128 bytes to 64×4 = 256 bytes. Compared to a 64-byte pixel payload, the feature doubles the bytes. Both calculations are correct for their respective representations; the report must state which is actually transmitted.

**11.7.**

Each long sequence uses 768 MiB; three require 2,304 MiB = 2.25 GiB. A 1.5 GiB cache budget does not suffice. Admission must account for prompt plus reserved generated continuation, other allocations, and realistic headroom.

**11.8.**

Quality: (784+198)/1,000 = .982. Cost: 3+.5+.2×12 = 5.9. Mean time: 45+5+.2×280 = 106 ms. Twenty percent take 330 ms, so the fixed-mixture p95 is 330 ms; the mean does not certify 300 ms tail latency.

**11.9.**

Accepted mass min(p,q) is (.2,.3,.1). Rejection mass .4 is resampled entirely onto the first token, giving (.6,.3,.1). Accepting all draft proposals gives q rather than p. The supplied categorical demonstration is not a full speculative LM.

**11.10.**

(40+N+30)/3 \< 50 implies N \< 80 ms. At 80 ms it only breaks even. K counts confirmed progress, so extra proposals can increase rejected work without useful advancement. This serial estimate omits overlap and variability.

**11.11.**

A pre-request router normally has request features but no complete candidate answer. A speculative verifier has draft proposals and target evaluations. A multi-model selector already has candidate outputs and has spent their generation cost. Interfaces and budgets must reflect those differences.

**11.12.**

4,000,000×2 = 8 MB per direction, 16 MB/client/round, 320 MB for 20 clients per round, and 3.2 GB for ten rounds (decimal units). This accounts for an assumed adaptation exchange, not inference traffic; the base artifact, protocol overhead, retries and compression are excluded.

**11.13.**

Use synthetic evidence. Verify local model/version/configuration, disconnect the WAN, then test an already warm request, a process restart, and a cold host restart separately. Record necessary local data, identity, storage and interface dependencies. A local proxy, cached answer, or test double cannot establish actual offline inference.

**11.14.**

Fix an authorized task suite and permit only a specified sanitized subset to leave. Include changed filtering/time rules, missing evidence, and a WAN outage. Record quality, coverage, total calls/tokens, end-to-end timing and resource/cost assumptions. Test-double runs validate plumbing, not comparative model quality.

(appendix-c-c-12-chapter-12)=

## C.12 Chapter 12

**12.1.**

A fixed dashboard still follows a developer-selected path; the language model changes presentation. In the second design the model chooses some next operations from an allowed set based on the goal and observed results. That adds flexibility and evaluation burden, not automatic superiority. Compare both on the same tasks and resource budget.

**12.2.**

A useful entry identifies a stream, owner/scope, coordinate frame, acceleration unit, timestamp/time zone, sampling policy, available interval, validity flags and schema version. The planner first needs meanings, available intervals and supported tools, not all raw acceleration rows. Access still comes from a trusted principal, not the catalog text.

**12.3.**

Private passages may already have entered a retrieval result, prompt, cache or log. Apply access filtering before ranking or at an equivalent protected retrieval boundary, then pass only authorized passages to generation. Check again before result release if authority can change. Never rely on the model to discard secrets after reading them.

**12.4.**

A snapshot defines the evidence version; losing it can make reproduction impossible or require a new task. The task record preserves completed operations, result IDs and budget; losing it creates uncertainty about progress. A KV cache accelerates one inference context and can often be rebuilt from permitted context; it is not a durable proof of tool completion. Rebuilding it has a cost and requires remaining context.

**12.5.**

The predicate selects pump-A:2 and pump-A:3, so the count is2. Those are two sampled instants. Counting distinct episodes requires explicit start/end, duration, gap and sampling rules. Neither two samples nor their one-minute spacing establishes a three-minute continuous event.

**12.6.**

Coverage is5/6≈83.33% over all queried slots, before activity filtering. The available active temperatures are22,23,25 and their arithmetic mean is70/3≈23.33 C. With a90% full-interval requirement, return insufficient\_evidence and the coverage/gap; do not present that arithmetic mean as an accepted task result. A different denominator requires an explicit different contract.

**12.7.**

Check the asset, time window, unit, input version, missing-data rule, filter, aggregation and meaning of the requested outcome. Verify that numeric claims match executed results and that all required qualifications appear. A program can execute correctly while answering the wrong question; a valid citation can accompany false prose.

**12.8.**

The original non-final-model cost is0.4+1.2+0.3+0.8+0.2=2.9 s. Adding0.7 s leaves6.0−2.9−0.7=2.4 s. A new six-second per-call allowance would exceed the complete-task budget. Real cancellation and timing must be enforced by the actual interfaces.

**12.9.**

Serial lower bound:0.4+0.6+1.0+0.3=2.3 s. Parallel lower bound:0.4+max(0.6,1.0)+0.3=1.7 s. The predicted saving0.6 s assumes independence and spare resources. Shared storage/CPU contention, queueing, launch overhead or a hidden dependency can reduce or remove it.

**12.10.**

Record job ID, owner, logical operation ID, canonical operation/arguments, immutable snapshot ID, status and durable result. Recheck current permission before replay. Identical operation/arguments can return the committed result; changed arguments require a new operation ID. A physical effect additionally needs device-supported identity/acknowledgment and unknown-outcome handling. Local persistence cannot provide remote exactly-once action semantics.

**12.11.**

A new offline question could compare two permitted intervals in locally retained history using installed tools and the local model. A request for the latest remote manual revision must stop or explicitly report the cached revision. State the surviving task family and dependencies. An offline mode is not established solely by using a loopback model URL.

**12.12.**

Compare task correctness, evidence coverage, completed/abstained tasks, whole-task latency, calls/tokens, memory, communication and failures at matched allowances. Extra agents are justified only by measured capability or parallelism/authority needs that outweigh coordination and error propagation. Repeated agreement is not independent evidence.

**12.13.**

A fresh default run gives count2 above28; changing to30 gives1. An expression with a call such as abs(temperature\_c) must be rejected because calls are absent from the small language. Save input, proposal, error category and actual result. The planner is a scripted test double in these runs, so the outcomes do not measure LM planning quality.

**12.14.**

Reserve combinations not used while developing prompts: another interval, a changed threshold and output unit, cross-asset comparison with missing coverage, ambiguous episode semantics, denied scope, and a post-commit restart. Write expected facts and required qualifications beforehand. Report per-case execution, semantic outcome and intervention; use additional independent cases for final claims after development inspection.

(appendix-c-c-13-chapter-13)=

## C.13 Chapter 13

**13.1.**

Draw phone → authorized local store → analysis/model, with an optional approved outbound path. Device ownership, site operator and remote provider can be separate authorities. Enforce the user’s permitted subject, interval and purpose before retrieving data into model context; output filtering cannot undo disclosure that already happened.

**13.2.**

Bind the verified signing key to a registered sensor identity and allowed assets/sites, then check that the requested operation is observation reporting. The site field is not its own authorization. A key binding proves a source relationship under the enrollment assumptions, not the physical truth of the value.

**13.3.**

With a correct local clock and no revocation-update path, a cached policy may keep accepting the grant until 09:15: up to 14 minutes after central revocation. Requiring a live decision can stop the operation throughout the outage. Choose by operation: cached read-only history may be permitted while a new privileged action is unavailable. State clock uncertainty, restart persistence, credential renewal and policy version.

**13.4.**

Unsigned payload: 100×24 = 2,400 B/s. Per-record signatures: 100×(24+64) = 8,800 B/s. Ten-record batches: 10×(10×24+64) = 3,040 B/s. Ten samples span nine 10-ms intervals, so the first sample may wait 90 ms. These figures omit encoding, headers, key identifiers, transport and verification costs; batching also couples delivery and validation of several samples.

**13.5.**

The version can be incompatible with the target or below an accepted security sequence floor. Accuracy alone does not establish freedom from a known vulnerability. Authorized recovery can package a previously working payload in a newly approved transition with a fresh security sequence; it should not permit arbitrary replay of an old signed envelope. The lab verifies eligibility, not installation.

**13.6.**

Secure boot restricts which startup software is accepted; runtime isolation restricts interactions while programs run; remote attestation supplies evidence about a target for another party’s appraisal. The mechanisms have different roots and freshness assumptions. None alone proves that a sensor is calibrated, a model’s diagnosis is correct, or a physical command is safe in current conditions.

**13.7.**

The totals are 4×23 = 92 and 5×24 = 120, so the added value is 28. Two permitted-looking aggregates can jointly disclose an individual contribution. Query history, overlapping cohorts and auxiliary information matter; suppressing names from each answer does not settle privacy.

**13.8.**

Treat the approval as referring to state version 7. Reject or pause when version 8 is observed, obtain fresh evidence and re-evaluate under the operation policy. Do not silently substitute the new state. Approval authenticates a decision under conditions; it does not establish that those conditions still hold. A real safety controller must enforce its own independently justified bounds.

**13.9.**

Precision = 90/(90+99) = 47.62%; recall = 90/(90+10) = 90%; accuracy = (90+9,801)/10,000 = 98.91%. Precision answers the investigation question for this population. Changing incident prevalence changes that interpretation even with similar conditional error rates. These are hypothetical counts.

**13.10.**

A device can send buffered historical records after reconnection at the same rate as an abusive sender. Useful evidence includes authenticated source scope, stable event identifiers, old event times, schema validity and total admitted work. A bounded response can limit intake rate, preserve an essential queue and request review, rather than irrevocably disconnect every bursty device.

**13.11.**

The authorized test signer really signs the fabricated 99°C value. Signature verification establishes the signed bytes under that key; scope checking establishes permission to report for the subject; neither establishes actual temperature. Independent calibration, cross-sensor checks or physical inspection would support different claims. The successful acceptance is a deliberate negative control.

**13.12.**

No. File permissions and accelerator scheduling address different properties. Measure the essential service’s response time, admitted work and memory while the other tenant is active. Bound concurrent accelerator work or use an enforceable allocation supported by the platform; keep enough headroom for essential work. Do not claim a hard deadline merely from a CPU or memory limit.

(appendix-c-c-14-chapter-14)=

## C.14 Chapter 14

**14.1.**

An internal log may have one accepted operator, so authenticated writes, backups and audit can be sufficient. A cross-manufacturer registry may require independent issuer roles and jointly governed acceptance. State whether all parties accept one ordering authority, who can correct records, and how omissions or conflicting views are detected. Several organizations alone do not force a blockchain.

**14.2.**

The replacement digest can match the replacement file perfectly. Obtain the expected digest from a trusted signed manifest, a pinned release record or another authenticated reference independent of the changed pair. The comparison still proves byte agreement, not that the program is suitable or defect-free.

**14.3.**

Examples include the installed unit’s identity, currently loaded software, calibration or physical condition, owner authorization, and present compromise status. Model certification concerns a product/model assertion under its stated scope; the installation process and operation need additional evidence.

**14.4.**

An inclusion proof connects a record to the supplied root. It does not establish that no later root exists, or that every reader received the same root. A trusted checkpoint, consistency checking and appropriately independent monitoring address other parts of the problem. The root’s authority must itself be established.

**14.5.**

The minimum overlap is 3+3−4 = 2. With at most one Byzantine participant, at least one overlapping participant is honest. The safety argument still needs honest-vote/locking rules that prevent that participant from supporting conflicting commits under the full protocol. Merely collecting three signatures is not a complete consensus algorithm.

**14.6.**

Each group can read its previously committed local state, marked with its freshness. A client can submit or queue a proposal, but two votes cannot meet the three-vote rule for a new commit. Restoring connectivity may restore progress subject to the protocol and resource assumptions. Do not report queued submission as shared acceptance.

**14.7.**

Raw application payload is 1,000×200×86,400 = 17,280,000,000 B/day, or 17.28 decimal GB. Metadata is 1,000×768 = 768,000 B/day, or 0.768 MB. Their ratio is 22,500. Four full payload copies total 69.12 GB/day before headers and storage overhead. The metadata does not preserve all raw observations; this is a choice of shared information, not lossless compression.

**14.8.**

Given appropriate interfaces and trusted keys, the program can check issuer role, signature or endorsement policy, fields, version, digest references and allowed state transitions. It cannot independently observe that a physical inspection took place or was competent. An external tester/oracle supplies a statement; the application must identify its authority and limitations.

**14.9.**

Public reading describes access to information; permissioned writing describes who can submit allowed changes; validator governance determines participants and accepted-history rules. A sensor can benefit through an authenticated gateway query without validating the ledger. That arrangement trusts the gateway or endpoint; independent verification requires a supported proof path and trusted state, not just received JSON.

**14.10.**

No. A newer revocation can exist outside the reader’s current view. A cached-grant policy can allow an explicitly bounded read-only operation until age 60 seconds, then refuse; sensitive new actions may instead require online confirmation immediately. The 20-second-old signature proves an issuer’s prior assertion, not the absence of later changes.

**14.11.**

Without an anchor, a valid prefix and two separately signed forks can each pass signature-and-link checks. A checkpoint at record 2a rejects histories that omit or disagree with that anchored position. A checkpoint at record 1 cannot select between later branches. The lab supplies no distributed agreement, complete view-change protocol, newest-state service or trustworthy checkpoint-distribution mechanism.

**14.12.**

Include task ID, requester/provider identity, input digest, model/artifact version, result digest, declared usage and timestamps, and sign the intended receipt context. A requester acknowledgment can establish receipt of named bytes. Actual usage needs agreed instrumentation; correctness needs task validation or stronger evidence appropriate to the application. A provider signature by itself does not prove honest metering or correct inference.

