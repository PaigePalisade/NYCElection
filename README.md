# Condorcet Voting vs Instant Runoff Voting in Real World Elections

How to use this application with New York City Elections

1. Run `fetch_ballots.py`. By default, it will look for the Dem Mayoral Primary votes. This will generate a ballots.pickle file which contains the ballots in a much more compressed and easy to read format.
2. Run `get_ids.py`. This will get a list of ids, copy them to the index2id array in `main.py`.
3. Run `main.py` to generate the tables.

Requires openpyxl module

## 2025 results
|                      | Zohran Kwame Mamdani | Brad Lander | Adrienne E. Adams | Andrew M. Cuomo | Zellnor Myrie | Scott M. Stringer | Michael Blake | Jessica Ramos | Whitney R. Tilson | Selma K. Bartholomew | Paperboy Love Prince |
|----------------------|----------------------|-------------|-------------------|-----------------|---------------|-------------------|---------------|---------------|-------------------|----------------------|----------------------|
| Zohran Kwame Mamdani |                    0 |      301606 |            386402 |          129940 |        515864 |            439922 |        579840 |        572124 |            560877 |               615951 |               621947 |
| Brad Lander          |              -301606 |           0 |            339795 |           85389 |        502665 |            437375 |        543463 |        538333 |            553334 |               587638 |               603675 |
| Adrienne E. Adams    |              -386402 |     -339795 |                 0 |            5793 |        286157 |            307913 |        411707 |        464835 |            489261 |               526905 |               536308 |
| Andrew M. Cuomo      |              -129940 |      -85389 |             -5793 |               0 |        105912 |            255863 |        252508 |        383439 |            432933 |               443813 |               442431 |
| Zellnor Myrie        |              -515864 |     -502665 |           -286157 |         -105912 |             0 |             84751 |        243734 |        291928 |            329181 |               366190 |               380944 |
| Scott M. Stringer    |              -439922 |     -437375 |           -307913 |         -255863 |        -84751 |                 0 |         71321 |        199291 |            232210 |               279449 |               280005 |
| Michael Blake        |              -579840 |     -543463 |           -411707 |         -252508 |       -243734 |            -71321 |             0 |        112102 |            167768 |               208208 |               214866 |
| Jessica Ramos        |              -572124 |     -538333 |           -464835 |         -383439 |       -291928 |           -199291 |       -112102 |             0 |             57637 |                93801 |                97701 |
| Whitney R. Tilson    |              -560877 |     -553334 |           -489261 |         -432933 |       -329181 |           -232210 |       -167768 |        -57637 |                 0 |                35614 |                41486 |
| Selma K. Bartholomew |              -615951 |     -587638 |           -526905 |         -443813 |       -366190 |           -279449 |       -208208 |        -93801 |            -35614 |                    0 |                 2827 |
| Paperboy Love Prince |              -621947 |     -603675 |           -536308 |         -442431 |       -380944 |           -280005 |       -214866 |        -97701 |            -41486 |                -2827 |                    0 |