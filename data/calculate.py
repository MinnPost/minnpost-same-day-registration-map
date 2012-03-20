import csv

r = csv.reader(open('2008_general_results_cut.csv', 'rU'));
out = csv.writer(open('2008_general_results_calculated.csv', 'wb'));

# Write header row
out.writerow(r.next() + ['CTUPRE', '7AMPercent', 'EDRPercent', 'PRPercent', 'PDPercent', 'CRPercent', 'CDPercent', 'MNRPercent', 'MNDPercent']);

for line in r:
    try:
        ctupre = str(int(line[3])) + ':' + str(int(line[0]))
    except ValueError:
        break
    pre_registered = int(line[4])
    edr = int(line[5])
    signatures = int(line[6])
    tot_votes = int(line[7])
    uspres_votes_r = int(line[8])
    uspres_votes_d = int(line[9])
    uspres_tot = int(line[16])
    uscong_votes_r = int(line[25])
    uscong_votes_d = int(line[26])
    uscong_tot = int(line[28])
    mnleg_votes_r = int(line[30])
    mnleg_votes_d = int(line[31])
    mnleg_tot = int(line[33])
    pre_registered_voted = signatures - edr
    pre_registered_voted_percent = -1;
    edr_percent = -1;
    uspres_percent = -1;
    mnleg_percent_r = -1;
    mnleg_percent_d = -1;
    if tot_votes != 0:
        pre_registered_voted_percent = round( 100 * ((1.0 * pre_registered_voted) / tot_votes), 2)
        edr_percent = round(100 * ((1.0 * edr) / tot_votes), 2)
    if uspres_tot != 0:
        uspres_percent_r = round(100 * ((1.0 * uspres_votes_r) / uspres_tot), 2)
        uspres_percent_d = round(100 * ((1.0 * uspres_votes_d) / uspres_tot), 2)
    if uscong_tot != 0:
        uscong_percent_r = round(100 * ((1.0 * uscong_votes_r) / uscong_tot), 2)
        uscong_percent_d = round(100 * ((1.0 * uscong_votes_d) / uscong_tot), 2)
    if mnleg_tot != 0:
        mnleg_percent_r = round(100 * ((1.0 * mnleg_votes_r) / mnleg_tot), 2)
        mnleg_percent_d = round(100 * ((1.0 * mnleg_votes_d) / mnleg_tot), 2)
    out.writerow(line + [ctupre, pre_registered_voted_percent, edr_percent, uspres_percent_r, uspres_percent_d, uscong_percent_r, uscong_percent_d, mnleg_percent_r, mnleg_percent_d])
