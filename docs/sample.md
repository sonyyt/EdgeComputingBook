# Typesetting sample: response-time budget

```{note}
This prototype reproduces selected text and Table 1.3 from section 1.6.1 of the
English v0.4.2 manuscript. It tests tables, mathematics, internal links, and
responsive layout. It is not the complete chapter. Figure 1.13 is not included
in this limited sample; the original table and equation identifiers are retained.
```

## 1.6.1 A response-time example

Suppose a teaching application classifies a captured image and should display the result within 200 ms. Assume that image preparation takes 20 ms in each design. We compare three placements for exactly the same classification task and assume comparable output quality. All values in Table 1.3 are invented teaching assumptions, not measurements of a product or requirements for a real production line.

(table-response-budget)=
**Table 1.3. An assumed end-to-end response-time budget**

| Time component | On device | Site server | Remote cloud |
| --- | --- | --- | --- |
| Image preparation | 20 ms | 20 ms | 20 ms |
| Network exchange, excluding queueing | 0 ms | 10 ms | 80 ms |
| Waiting for execution | 0 ms | 15 ms | 30 ms |
| Classification | 120 ms | 35 ms | 15 ms |
| Total | 140 ms | 80 ms | 145 ms |

$$
T_{\mathrm{response}} = T_{\mathrm{prepare}} + T_{\mathrm{network}} + T_{\mathrm{wait}} + T_{\mathrm{compute}} \tag{1.1}
$$

Here T_network includes the request and result transfers and their path delay. Any network queueing included in that measurement must not be counted again in T_wait; in this example T_wait means waiting for execution at the selected host.

All three designs meet the assumed 200 ms target, and the site server has the shortest total in this example. It would still be premature to conclude that it is the best overall design. The on-device option needs no local application server; the remote option may simplify site maintenance; the shared site server may become busy when more cameras arrive. If its waiting time increases from 15 ms to 150 ms, its total rises to 215 ms and misses the target.

The next step is an experiment under the workload that matters: measure the complete response, vary the arrival rate, and record missed targets as well as successful responses. If raw images are not allowed to leave the premises, the remote design in the table may also be unacceptable regardless of its speed. Requirements help identify both feasibility and performance; they should not be replaced by one average latency number.

## Navigation check

This is a website-only navigation check: return to [Table 1.3](#table-response-budget)
or read the [Preface](preface.md). These links are not additional textbook content.
