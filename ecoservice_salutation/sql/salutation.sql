UPDATE res_partner_title
SET salutation = 'Dear Sir'
WHERE name = 'Sir';

UPDATE ir_translation
SET value = 'Sehr geehrter Herr'
WHERE src = 'Dear Sir';

UPDATE res_partner_title
SET salutation = 'Dear Mrs.'
WHERE name = 'Madam';

UPDATE ir_translation
SET value = 'Sehr geehrte Frau'
WHERE src = 'Dear Mrs.';