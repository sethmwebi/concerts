from __init__ import close_connection, get_connection


class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id
        self.conn = get_connection()

    def band(self):
        query = """
        SELECT bands.* 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        WHERE concerts.id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.concert_id,))
            return cur.fetchone()

    def venue(self):
        query = """
        SELECT venues.* 
        FROM concerts 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.concert_id,))
            return cur.fetchone()

    def hometown_show(self):
        query = """
        SELECT (bands.hometown = venues.city) 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.concert_id,))
            return cur.fetchone()[0]

    def introduction(self):
        query = """
        SELECT bands.name, bands.hometown, venues.city 
        FROM concerts 
        JOIN bands ON concerts.band_id = bands.id 
        JOIN venues ON concerts.venue_id = venues.id 
        WHERE concerts.id = %s;
        """
        with self.conn.cursor() as cur:
            cur.execute(query, (self.concert_id,))
            band_name, band_hometown, venue_city = cur.fetchone()
            return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"

    def __del__(self):
        close_connection(self.conn)
