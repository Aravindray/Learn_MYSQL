for (i = 1; i <= session.sql("SELECT MAX(arms) AS maxarms FROM limbs").execute().fetchOne().getField('maxarms'); i++) {
    species = session.sql("SELECT COUNT(*) AS countarms FROM limbs WHERE arms = ?").bind(i).execute();
    if (species.hasData() && (armscount = species.fetchOne().getField('countarms')) > 0) {
        print("We have " + armscount + " species with " + i + (i == 1 ? " arm\n": " arms\n"));
    }
}
