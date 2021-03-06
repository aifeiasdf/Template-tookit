from template.test import TestCase, main


class ThrowTest(TestCase):
  def testThrow(self):
    self.Expect(DATA, None)


DATA = r"""
-- test --
[% me = 'I' -%]
[% TRY -%]
   [%- THROW chicken "Failed failed failed" 'boo' name='Fred' -%]
[% CATCH -%]
ERROR: [% error.type %] - [% error.info.0 %]/[% error.info.1 %]/[% error.info.name %]
[% END %]
-- expect --
ERROR: chicken - Failed failed failed/boo/Fred

-- test --
[% TRY -%]
[% THROW food 'eggs' -%]
[% CATCH -%]
ERROR: [% error.type %] / [% error.info %]
[% END %]

-- expect --
ERROR: food / eggs

# test throwing multiple params
-- test --
[% pi = 3.14
   e  = 2.718 -%]
[% TRY -%]
[% THROW foo pi e msg="fell over" reason="brain exploded" -%]
[% CATCH -%]
[% error.type %]: pi=[% error.info.0 %]  e=[% error.info.1 %]
     I [% error.info.msg %] because my [% error.info.reason %]!
[% END %]
-- expect --
foo: pi=3.14  e=2.718
     I fell over because my brain exploded!

-- test --
[% TRY -%]
[% THROW foo 'one' 2 three=3.14 -%]
[% CATCH -%]
   [% error.type %]
   [% error.info.0 %]
   [% error.info.1 %]
   [% error.info.three %]
   [%- FOREACH e = error.info.args %]
   * [% e %]
   [%- END %]
[% END %]
-- expect --
   foo
   one
   2
   3.14
   * one
   * 2

-- test --
[% TRY -%]
[% THROW food 'eggs' 'flour' msg="Missing Ingredients" -%]
[% CATCH food -%]
   [% error.info.msg %]
[% FOREACH item = error.info.args -%]
      * [% item %]
[% END -%]
[% END %]
-- expect --
   Missing Ingredients
      * eggs
      * flour



"""

main()
